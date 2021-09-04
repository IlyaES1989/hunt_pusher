import aiohttp


class Dispatcher:
    def __init__(self, token, endpoint):
        self.token = token
        self.endpoint = endpoint
        self.headers = {'Authorization': f'Bearer {self.token}'}

        self.account_id = int()
        self.applicant_id = int()
        self.stages = {}
        self.vacancies = {}

    def _set_vacancy_request(self, **kwargs):
        title = kwargs.get('vacancy')
        raw_status = kwargs.get('raw_status')
        comment = kwargs.get('comment')
        return {
            'vacancy': self.vacancies.get(f'{title}'),
            'status': self.stages.get(f'{raw_status}'),
            'comment': comment,
        }

    @staticmethod
    def _set_file_request(file, file_name):
        return {
            'name': 'file',
            'value': file,
            'filename': file_name,
        }

    async def get_account(self, client):
        url = f'{self.endpoint}/accounts'
        async with client.get(url) as resp:
            assert resp.status == 200
            accounts = await resp.json()
            account = accounts.get('items')[0]
            self.account_id = account.get('id')
            return self.account_id

    async def get_stages(self, client):
        url = f'{self.endpoint}/account/{self.account_id}/vacancy/statuses'
        async with client.get(url) as resp:
            assert resp.status == 200
            stages = await resp.json()

            self.stages = {
                stage.get('name'): stage.get('id')
                for stage in stages.get('items')
            }
            return self.stages

    async def get_vacancies(self, client):
        url = f'{self.endpoint}/account/{self.account_id}/vacancies'
        async with client.get(url) as resp:
            assert resp.status == 200
            raw_vacancies = await resp.json()

            self.vacancies = {
                vacancy.get('position'): vacancy.get('id')
                for vacancy in raw_vacancies.get('items')
            }
            return self.vacancies

    async def upload_cv(self, client, file=None, file_name=None):
        url = f'{self.endpoint}/account/{self.account_id}/upload'

        client.headers.update(**{'X-File-Parse': "true", })

        data = aiohttp.FormData()
        file = self._set_file_request(file, file_name)
        data.add_field(**file)

        async with client.post(url, data=data) as resp:
            # assert resp.status == 200
            return await resp.json()

    async def set_applicant(self, client, request):
        url = f'{self.endpoint}/account/{self.account_id}/applicants'
        async with client.post(url, json=request) as resp:
            assert resp.status == 200
            applicant = await resp.json()
            self.applicant_id = applicant.get('id')
            return self.applicant_id

    async def post_vacancy(self, client, **kwargs):
        url = f'{self.endpoint}/account/{self.account_id}/applicants/{self.applicant_id}/vacancy'
        request = self._set_vacancy_request(**kwargs)

        async with client.post(url, json=request) as resp:
            assert resp.status == 200
            return await resp.json()
