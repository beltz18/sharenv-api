from controllers.connection import db
from var.collections        import *

def createSpace(u,s,i):
  """
  This function creates a new space with a given name and owner, and checks if the owner exists in the
  user database.
  
  :param u: The username of the owner of the space being created
  :param s: The name of the space to be created
  :param i: The parameter "i" represents a list of users who are invited to the space
  :return: a dictionary with two keys: 'message' and 'status'. The value of 'message' depends on the
  conditions met in the function. If a space with the given name already exists, the message will be
  "Space {s} already exists". If the user does not exist or is not logged in, the message will be "To
  create a space you need to create a user
  """
  space   = {
    'name': s,
    'owner' : u,
    'invited': [i],
    'files': []
  }
  ifUser    = userDb.find_one({ 'user': u  })
  ifInvited = userDb.find_one({ 'user': i  })
  ifSpace   = spaceDb.find_one({ 'name': s })

  if ifUser:
    if ifSpace:
      return {
        'message': f'Space {s} already exists',
        'status': False
       }
    if i == u:
      return {
        'message': 'You cannot invite yourself to a Space',
        'status': False
      }
    if not ifInvited:
      return {
        'message': "The person that has been invited doesn't have an account",
        'status': False
      }
    spaceDb.insert_one(space)
    return {
      'message': f'Space {s} created successfully',
      'status': True
    }
  else:
    return {
      'message': 'To create a space you need to create a user first, or log in with your username',
      'status': False
    }
  
def listSpaces(u):
  """
  The function returns a list of spaces owned and invited for a given user.
  
  :param u: The parameter 'u' is a string representing the username of the user whose spaces are being
  listed
  :return: A dictionary containing either the spaces owned and invited by the user, along with a
  message and a status of True if the user exists in the database, or a message and a status of False
  if the user does not exist in the database.
  """
  ifUser        = userDb.find_one({ 'user': u })
  spaceOwner    = spaceDb.find({ 'owner':   u })
  invitedSpaces = spaceDb.find({ 'invited': u })
  dataOwner     = []
  dataInvited   = []

  for space in spaceOwner:
    dataOwner.append(space['name'])
  for space in invitedSpaces:
    dataInvited.append(space['name'])

  if ifUser:
    return {
      'data': {
        'spacesOwned': dataOwner, 
        'spacesInvited': dataInvited
      },
      'message': 'Your spaces',
      'status': True 
    }
  else:
    return {
     'message': "User doesn't exist",
     'status': False
    }

def updateSpace(s,u):
  """
  This function updates a space by adding a user to its list of invited members.
  
  :param s: The name of the space to which a user is being invited
  :param u: The parameter 'u' represents the user who is being invited to a space
  :return: a dictionary with a message and a status indicating whether the user was successfully added
  to the space or not. The message provides information about the outcome of the function, while the
  status is a boolean value (True or False) indicating whether the operation was successful or not.
  """
  # s = space name
  # u = user invited to space
  ifSpace  = spaceDb.find_one({ 'name':    s })
  ifExists = userDb.find_one( { 'user':    u })
  ifUser   = spaceDb.find_one({ 'name': s, 'invited': u })
  ifOwner  = spaceDb.find_one({ 'name': s, 'owner': u })

  if ifSpace:
    # Check if user exists
    if ifExists:
      # Check if user is part of the space
      if ifUser:
        return {
          'message': 'This user is already part of this Space',
          'status': False
        }
      
      # Check if user invited is owner
      if ifOwner:
        return {
          'message': 'You cannot invite yourself to your own space',
          'status': False
        }
    
      spaceDb.find_one_and_update(
        {'name': s},
        {'$push': { 'invited': u }}
      )

      return {
        'message': f'User {u} added to space {s}',
        'status': True
      }
    else:
      return {
        'message': "The specified user doesn't exist",
        'status': False
      }
    
  else:
    return {
      'message': "This space doesn't exist",
      'status': False
    }
    
def renameSpace(s,u,n):
  """
  This function renames a space in a database and returns a message indicating success or failure.
  
  :param s: The current name of the space that needs to be renamed
  :param u: The owner of the space being renamed
  :param n: The new name for the space
  :return: A dictionary containing a message and a status. The message indicates whether the space was
  successfully renamed or not, and the status indicates whether the operation was successful or not.
  """
  if spaceDb.find_one_and_update(
    { 'owner': u, 'name': s },
    { '$set': { 'name': n } }
  ):
    return {
      'message': f"Space '{s}' renamed as '{n}'",
      'status': True
    }
  else:
    return {
      'message': "No such space found or you don't have access.",
      'status': False
    }

def deleteSpace(n,u):
  """
  This function deletes a space from a database if it exists and is owned by a specified user.
  
  :param n: The name of the space to be deleted
  :param u: The parameter 'u' is likely a variable representing the owner of a space in a database
  :return: The function `deleteSpace` returns a dictionary with two keys: `message` and `status`. The
  value of `message` depends on whether the space with the given name and owner was successfully
  deleted or not. If it was deleted, the message will say "Space '{n}' deleted", where `{n}` is the
  name of the space. If it was not deleted, the message will say
  """
  if spaceDb.find_one_and_delete({ 'name': n, 'owner': u }):
    return {
      'message': f"Space '{n}' deleted",
      'status': True
    }
  else:
    return {
      'message': "You do not own this space or don't exists",
      'status': False
    }