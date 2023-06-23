from flask            import *
from var.vars         import *
from controllers.user import *
from flask_cors       import CORS

app = Flask(__name__)
app.secret_key = SECRET
CORS(app)

@app.route(ROOT)
def index():
  return 'API running...'

@app.route(CREATE_U, methods=['POST'])
def create_user():
  """
  This function creates a new user with a username and password provided in a JSON request and returns
  the result of the createUser function.
  :return: the output of the `createUser` function, which is presumably creating a new user with the
  provided username and password. The specific output of `createUser` is not shown in the code snippet
  provided.
  """
  if request.method == 'POST':
    print(request.form)
    user = request.json['user']
    pasw = request.json['pasw']
    a = createUser(user,pasw)
    return a

@app.route(AUTH_U, methods=['POST'])
def auth_user():
  """
  This function authenticates a user by checking their username and password in a POST request.
  :return: the output of the `authUser()` function, which is not specified in the given code. It is
  likely that `authUser()` is a custom function that authenticates the user based on the provided
  username and password.
  """
  if request.method == 'POST':
    print(request.form)
    user = request.json['user']
    a = authUser(user)
    return a

if __name__ == '__main__':
  app.run()