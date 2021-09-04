# Hunt pusher
Скрипт собирает данные по кандидатам на вакансию, добавляет их в базу и добавляет кандидатов на вакансию.

## Запуск проекта
```
pip install -r requirements.txt

python main.py
```

```
usage: main.py [-h] [-t TOKEN] [-e ENDPOINT] [-f FILE] [-c CV]

optional arguments:
  -h, --help            show this help message and exit
  -t TOKEN, --token TOKEN
                        Personal token. Read more https://github.com/huntflow/api/blob/master/en/personal_token.md
  -e ENDPOINT, --endpoint ENDPOINT
                        Basic URL to call HuntFlowAPI
  -f FILE, --file FILE  Excel file with list of applicants
  -c CV, --cv CV        Path to storage of CVs

```
