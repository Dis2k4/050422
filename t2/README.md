Для выполнения теста требуются библиотеки python-dotenv, PyGithub.
Для установки требуемых пакетов выполнить в командной строке:
pip install -r requirements.txt

Переименовать файл test_api.env.demo из папки проекта в test_api.env
Входные данные передаются через файл конфигурации test_api.env.
В файле конфигурации переменные соответствуют:
GitUserName - имя пользователя GitHub
Token - токен API
RepoName - имя репозитория
