import os
import time
from dotenv import load_dotenv
from github import Github

dotenv_path = os.path.join(os.path.dirname(__file__), 'test_api.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

GitUserName = os.getenv("GitUserName")
Token = os.getenv("Token")
RepoName = os.getenv("RepoName")

#создаем репозиторий
g = Github(Token)
user = g.get_user()
repo = user.create_repo(name=RepoName)

#ищем созданный репозиторий
time.sleep(5)
user = g.get_user(GitUserName) 
assert repo in g.search_repositories(RepoName), "Репозиторий не создался"

#удаляем репозиторий
user = g.get_user(GitUserName) 
repo = user.get_repo(RepoName)
repo.delete()

#проверяем что репозиторий удален
user = g.get_user(GitUserName) 
assert not(repo in g.search_repositories(RepoName)), "Репозиторий не удалился"

print("Everything passed")