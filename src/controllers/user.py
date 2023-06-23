from controllers.connection import db

def createUser(u,p):
  """
  The function creates a new user in a database if the user does not already exist.
  
  :param u: The username of the user being created
  :param p: The parameter 'p' in the 'createUser' function is the password for the user being created
  :return: The function `createUser(u,p)` returns a dictionary with two keys: 'message' and 'status'.
  The value of 'message' depends on whether the user already exists in the database or not. If the
  user already exists, the message will say "User {user['user']} already exists". If the user does not
  exist, the message will say "User {user['user']} inserted
  """
  userDb = db.users
  user = {
    'user': u,
    'password' : p
  }
  ifUser = userDb.find_one({ 'user': user['user'] })
  
  if ifUser:
    return {
      'message': f"User {user['user']} already exists",
      'status': False
    }
  
  userDb.insert_one(user)
  return {
    'message': f"User {user['user']} inserted",
    'status': True
  }

def authUser(u):
  """
  The function `authUser` checks if a user exists in a database and returns a message indicating
  whether the user is authenticated or not.
  
  :param u: The username of the user trying to authenticate
  :param p: The parameter "p" in the "authUser" function is a string representing the password of the
  user
  :return: The function `authUser(u,p)` returns a dictionary with two keys: 'message' and 'status'.
  The value of 'message' depends on whether the user exists in the database or not. If the user
  exists, the message will say "User {user['user']} authenticated". If the user doesn't exist, the
  message will say "User {user['user']} doesn't exists".
  """
  userDb = db.users
  user = { 'user': u }
  ifUser = userDb.find_one(user)
  
  if ifUser:
    return {
      'data': ifUser,
      'message': f"User {user['user']} authenticated",
      'status': True
    }
  else: 
    return {
      'message': f"User {user['user']} doesn't exists", 
      'status': False
    }