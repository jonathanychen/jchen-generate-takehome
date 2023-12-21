import requests
import json

BASE_URL = "https://generate-coding-challenge-server-rellb.ondigitalocean.app"
NAME = "Jonathan Chen"
NUID = "002131787"

class APIMethods:
    @staticmethod
    def register():
        payload = {"name": NAME, "nuid": NUID}
        response = requests.post(f"{BASE_URL}/register", json=payload)
        with open("challenge.txt", 'wb') as fd:
            for chunk in response.iter_content(chunk_size=128):
                fd.write(chunk)

    @staticmethod
    def forgot_token():
        response = requests.get(f"{BASE_URL}/forgot_token/{NUID}")
        body = response.json()
        print(body)

    @staticmethod
    def submit_solution(solution: list):
        with open("challenge.txt", "r") as f:
            challenge_data = json.load(f)
        token = challenge_data['token']
        response = requests.post(f"{BASE_URL}/submit/{token}", json=solution)
        print(response.status_code, response.text)