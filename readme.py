from github import Github
import requests
from hamconf import parse_file
import re as regex

config = parse_file('config.hamconf')
username = config.get('CONFIG.username')
repo_name = config.get('CONFIG.repo_name')
token = config.get('SECRETS.PERSONAL_GITHUB_TOKEN')
fact_reg = r'(<fact>)(.|\n)*(<\/fact>)'

def get_blob_sha() -> str:
	with requests.get(f'https://api.github.com/repos/{username}/{repo_name}/contents/README.md') as r:
		return r.json().get('sha')


def get_contents(fact: str) -> str:
	with requests.get(f'https://raw.githubusercontent.com/{username}/{repo_name}/master/README.md') as r:
		data = r.text
	data = regex.sub(fact_reg, f'<fact>{fact}</fact>', data)
	return data


def insert_fact(fact: str):
	gh = Github(token)

	data = get_contents(fact)

	sha = get_blob_sha()

	repo = gh.get_repo(f'{username}/{repo_name}')
	repo.update_file('README.md', 'Random-Fact bot', data, sha)

if __name__ == '__main__':
	insert_fact('Hello World')

