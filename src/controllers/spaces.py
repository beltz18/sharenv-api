from controllers.connection import db
from var.collections        import *

def createSpace(u,s,i=None):
  """
  This function creates a new space with a given name and owner, and invites specified users to the
  space.
  
  :param u: The user that is creating the space
  :param s: The name of the space that the user wants to create
  :param i: Users invited to the space. It is a list of usernames
  :return: a dictionary with two keys: 'message' and 'status'. The 'message' key contains a string
  message indicating the result of the operation, while the 'status' key contains a boolean value
  indicating whether the operation was successful or not.
  """
  space   = {
    'name': s,
    'owner' : u,
    'invited': [i]
  }
  ifUser  = userDb.find_one({ 'user': u })
  ifSpace = spaceDb.find_one({ 'name': s })

  if ifUser:
    if ifSpace:
      return {
        'message': f'Space {s} already exists',
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
  ifUser   = spaceDb.find_one({ 'invited': u })
  ifOwner  = spaceDb.find_one({ 'owner':   u })

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