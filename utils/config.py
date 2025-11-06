import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL = os.getenv('BASE_URL', 'https://dealwallet.com')
    TIMEOUT = int(os.getenv('TIMEOUT', '30000'))
    HEADLESS = os.getenv('HEADLESS', 'false').lower() == 'true'