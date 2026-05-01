from dotenv import load_dotenv
import os


load_dotenv()  # loads .env into environment

API_KEY = os.environ.get('nokiaApiKey')

headers = {
    'Content-Type' : 'application/json',
    'x-rapidapi-host' : 'network-as-code.nokia.rapidapi.com',
    'x-rapidapi-key' : API_KEY
    }
