from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL_UI = os.getenv("BASE_URL_UI", "https://the-internet.herokuapp.com")
BASE_URL_API = os.getenv("BASE_URL_API", "https://reqres.in/api")