from dotenv import load_dotenv
import os

load_dotenv()

SECRET    = os.getenv('SECRET')
ROOT      = os.getenv('ROOT')
CREATE_U  = os.getenv('CREATE_U')
AUTH_U    = os.getenv('AUTH_U')
MONGO_URI = os.getenv('MONGO_URI')
MONGO_DB  = os.getenv('MONGO_DB')
CREATE_S  = os.getenv('CREATE_S')
LIST_S    = os.getenv('LIST_S')
UPDATE_S  = os.getenv('UPDATE_S')