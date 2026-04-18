"""
Configuration for DealWallet Automation Framework
"""

import os

class Config:
    
    BASE_URL = "https://dealwallet.com"

    
    ENV = os.getenv("ENV", "production")

    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
    SLOW_MO = int(os.getenv("SLOW_MO", 100))

  
    PAGE_LOAD_TIMEOUT = 15000
    SHORT_WAIT = 2000
    LONG_WAIT = 5000

    ENABLE_LOGS = True