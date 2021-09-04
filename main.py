import aiohttp
import asyncio

from dispatcher import Dispatcher
from reader import Reader
from applicant import Applicant
from logger import logger
from cmd_args import parser

ARGS = parser.parse_args()
TOKEN = ARGS.token
ENDPOINT = ARGS.endpoint
CV_STORAGE = ARGS.cv
CV_BASE = ARGS.file


async def main(token, endpoint, path, cv_base):
    logger.info(f'Preparation for uploading the resumes.')
    dispatcher = Dispatcher(token, endpoint)
    connector = aiohttp.TCPConnector(limit=10)

    async with aiohttp.ClientSession(
            headers=dispatcher.headers,
            connector=connector) as client:

        await dispatcher.get_account(client)
        await dispatcher.get_stages(client),
        await dispatcher.get_vacancies(client),

        reader = Reader(cv_base, path,)
        try:
            while True:
                data = reader.data()

                logger.info('Start loading the resumes.')
                applicant = Applicant(**data)
                parsed_data = await dispatcher.upload_cv(
                    client,
                    applicant.file,
                    applicant.file_name
                )
                request = applicant.get_data(parsed_data)

                await dispatcher.set_applicant(client, request)
                await dispatcher.post_vacancy(client, **request)
                logger.info(f'The resume of {applicant.full_name} has been uploaded.')
        except StopIteration:
            reader.set_error(None)
            await asyncio.sleep(1)
            logger.info(f'Done!')
        except AssertionError:
            logger.warning(f'Error at the row #{reader.current_row}')
            reader.set_error(reader.current_row)


if __name__ == '__main__':

    asyncio.run(main(
        token=TOKEN,
        endpoint=ENDPOINT,
        path=CV_STORAGE,
        cv_base=CV_BASE
    ))

