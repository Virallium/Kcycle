
from getpass import getpass

import requests

endpoint = "http://localhost:8000/api/auth/token/"
credentials = {
	"username": input("Nom d'utilisateur: "),
	"password": getpass("Mot de passe: "),
}

try:
	response = requests.post(endpoint, json=credentials, timeout=10)
except requests.ConnectionError as error:
	raise SystemExit(
		"Serveur inaccessible. Lance d'abord Django avec "
		"'python manage.py runserver'."
	) from error

print(response.status_code)
try:
	print(response.json())
except requests.exceptions.JSONDecodeError:
	print(response.text)