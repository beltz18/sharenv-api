from dotenv import load_dotenv
import os

load_dotenv()

SECRET    = os.getenv('SECRET')
MONGO_URI = os.getenv('MONGO_URI')