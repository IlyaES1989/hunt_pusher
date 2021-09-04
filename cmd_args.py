import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-t', '--token',
                    help='Personal token.\n Read more https://github.com/huntflow/api/blob/master/en/personal_token.md',
                    default=input('Enter your personal token: ')
                    )

parser.add_argument('-e', '--endpoint',
                    help='Basic URL to call HuntFlowAPI',
                    default='https://dev-100-api.huntflow.dev',
                    )

parser.add_argument('-f', '--file',
                    help='Excel file with list of applicants',
                    default=input('Specify the Excel-file with list of applicants: ')
                    )

parser.add_argument('-c', '--cv',
                    help='Path to storage of CVs',
                    default=input('Specify a path to storage of CVs: ')
                    )
