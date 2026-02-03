# import os
# from dotenv import load_dotenv

# load_dotenv()

# class Config:
#     BASE_URL = os.getenv('BASE_URL', 'https://dealwallet.com')
#     TIMEOUT = int(os.getenv('TIMEOUT', '30000'))
#     HEADLESS = os.getenv('HEADLESS', 'false').lower() == 'true'

"""
Configuration for DealWallet Automation Framework
"""

# Base URL
BASE_URL = "https://dealwallet.com"

# Environment settings
ENV = "production"
HEADLESS = False  # Used by playwright to run browser in headless or headed mode
SLOW_MO = 100

# Timeouts
PAGE_LOAD_TIMEOUT = 15000
SHORT_WAIT = 2000
LONG_WAIT = 5000

# Logging flag
ENABLE_LOGS = True


# Optional backward-compatible Config class
class Config:
    BASE_URL = BASE_URL
    HEADLESS = HEADLESS
    SLOW_MO = SLOW_MO 
    ENV = ENV
 