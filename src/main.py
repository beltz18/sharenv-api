from flask              import *
from var.vars           import *
from controllers.user   import *
from controllers.spaces import *
from flask_cors         import CORS

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
    user = request.json['user']
    pasw = request.json['pasw']
    a    = createUser(user,pasw)
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
    user = request.json['user']
    a    = authUser(user)
    return a
  
@app.route(CREATE_S, methods=['POST'])
def create_space():
  """
  This function creates a space with the given owner, name, and invited members.
  :return: the output of the `createSpace()` function, which is stored in the variable `a`.
  """
  if request.method == 'POST':
    space   = request.json['space']
    owner   = request.json['owner']
    invited = request.json['invited']
    a       = createSpace(owner,space,invited)
    return a
  
@app.route(LIST_S, methods=['POST'])
def list_spaces():
  """
  This function takes a POST request with a JSON object containing a user parameter, calls the
  listSpaces function with the user parameter, and returns the result.
  :return: the result of calling the `listSpaces()` function with the `user` parameter that is
  obtained from the JSON data in the request. The specific data type and format of the returned value
  depends on the implementation of the `listSpaces()` function.
  """
  if request.method == 'POST':
    user = request.json['user']
    a    = listSpaces(user)
    return a

@app.route(UPDATE_S, methods=['POST'])
def update_space():
  """
  This function updates a space with invited users based on a POST request.
  :return: The variable `a` is being returned.
  """
  if request.method == 'POST':
    space   = request.json['space']
    invited = request.json['invited']
    a       = updateSpace(space, invited)
    return a
  
@app.route(RENAME_S, methods=['POST'])
def rename_space():
  """
  This function renames a space for a given user with a new name, using the input provided through a
  POST request.
  :return: the result of calling the `renameSpace()` function with the `space`, `user`, and `new_name`
  parameters that were obtained from the JSON data in the request. The specific value that is returned
  depends on the implementation of the `renameSpace()` function.
  """
  if request.method == 'POST':
    space    = request.json['space']
    user     = request.json['user']
    new_name = request.json['new_name']
    a        = renameSpace(space,user,new_name)
    return a

@app.route(DELETE_S, methods=['POST'])
def delete_space():
  """
  This function deletes a space owned by a specific owner based on a POST request with JSON data.
  :return: The variable `a` is being returned.
  """
  if request.method == 'POST':
    space  = request.json['space']
    owner  = request.json['owner']
    a      = deleteSpace(space,owner)
    return a

if __name__ == '__main__':
  app.run()