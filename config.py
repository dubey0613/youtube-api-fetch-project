import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    DATABASE_URL = os.getenv('DATABASE_URL')
    YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')