from dotenv import load_dotenv
import os

load_dotenv()

SECRET    = os.getenv('SECRET')
ROOT      = os.getenv('ROOT')
CREATE_U  = os.getenv('CREATE_U')
AUTH_U    = os.getenv('AUTH_U')
MONGO_URI = os.getenv('MONGO_URI')
MONGO_DB  = os.getenv('MONGO_DB')