from flask            import *
from var.vars         import *
from controllers.user import *

app = Flask(__name__)
app.secret_key = SECRET

@app.route('/')
def index():
  return 'API running...'

@app.route('/user/create')
def create_user():
  pass

@app.route('/user/auth')
def auth_user():
  pass