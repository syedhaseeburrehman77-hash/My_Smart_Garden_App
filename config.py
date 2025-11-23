"""
Configuration file for Smart Garden App
Loads environment variables and provides configuration settings
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Keys
# IMPORTANT: All API keys must be stored in .env file (which is gitignored)
# Never commit API keys to GitHub!
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
PERENUAL_API_KEY = os.getenv("PERENUAL_API_KEY", "")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY", "")

# Default Settings
DEFAULT_LOCATION = os.getenv("DEFAULT_LOCATION", "Sialkot,PK")
DEFAULT_CITY = "Sialkot"
DEFAULT_COUNTRY = "PK"

# API Endpoints
OPENWEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5"
PERENUAL_BASE_URL = "https://perenual.com/api"

# Data Storage
PLANTS_DB_FILE = "plants_database.json"
CHAT_HISTORY_FILE = "chat_history.json"

# App Settings
WATERING_CHECK_TIME = "08:00"  # Daily check time
MAX_PLANTS = 50  # Maximum number of plants user can add

