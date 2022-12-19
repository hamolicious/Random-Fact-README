import requests

def get_fact():
	with requests.get('https://uselessfacts.jsph.pl/today.json?langauge=en') as r:
		if r.status_code == 200:
			return r.json().get('text')


if __name__ == '__main__':
	print(get_fact())

