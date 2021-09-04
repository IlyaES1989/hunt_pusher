import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-t', '--token',
                    help='Personal token.\n Read more https://github.com/huntflow/api/blob/master/en/personal_token.md',
                    )

parser.add_argument('-e', '--endpoint',
                    help='Basic URL to call HuntFlowAPI',
                    default='https://dev-100-api.huntflow.dev',
                    )

parser.add_argument('-f', '--file',
                    help='Excel file with list of applicants',
                    )

parser.add_argument('-c', '--cv',
                    help='Path to storage of CVs',
                    )

ARGS = parser.parse_args()
ENDPOINT = ARGS.endpoint

TOKEN = ARGS.token
if not TOKEN:
    TOKEN = input('Enter your personal token: ')

CV_STORAGE = ARGS.cv
if not CV_STORAGE:
    CV_STORAGE = input('Specify a path to storage of CVs: ')

CV_BASE = ARGS.file
if not CV_BASE:
    CV_BASE = input('Specify the Excel-file with list of applicants: ')
