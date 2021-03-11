from starlette.testclient import TestClient
from main import app
import requests
from dotenv import load_dotenv
import os

load_dotenv() 
API_KEY = os.environ.get("API_KEY")

def test_weather_api():
    url = f"https://api.openweathermap.org/data/2.5/weather?q=London,UK&units=metric&appid={API_KEY}"
    response = requests.get(url)
    assert response.status_code == 200

def test_home():
    url = 'http://127.0.0.1:8000/home/'
    response = requests.get(url)
    assert response.status_code == 200

data = {
  "name": "John",
  "email": "John@test.com",
  "password": "$2b$12$VEj.a9P.gsd2hgZ9GFyXTOUzNCL3ajxN1uhimlNB9Ppyxe2Kn7JQ6",
  "city": "London",
  "country": "UK"
}

def test_get_user():
    url = 'http://127.0.0.1:8000/user/27'
    response = requests.get(url)
    assert response.text == data