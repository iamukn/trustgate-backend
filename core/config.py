from dotenv import load_dotenv
import os


load_dotenv()  # loads .env into environment

# API KEY AND HEADERS
API_KEY = os.environ.get('nokiaApiKey')
headers = {
    'Content-Type' : 'application/json',
    'x-rapidapi-host' : 'network-as-code.nokia.rapidapi.com',
    'x-rapidapi-key' : API_KEY
    }



# SimSwap Scores
TWENTY=20
FOURTY=40
FIFTY=50
FIFTY_EIGHT=58
SIXTY=60

# min and max risk score
MIN_RISK_SCORE=0
MAX_RISK_SCORE=100

# Numbers Verify
NUMBERS_VERIFY_SCORE = 30

# Device Status Score
DEVICE_STATUS_SCORE = 15

# THRESHOLD TO BLOCK OR CHALLENGE DURING DECISION
BLOCK=60
CHALLENGE=30
