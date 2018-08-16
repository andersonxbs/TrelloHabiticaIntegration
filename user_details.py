import os
import json

idOfList=''
trello_apiKey=''
trello_apiToken=''
habitica_users_by_trello_member_id={}

if "TRELLO_DONE_LIST_ID" in os.environ:
    idOfList=os.environ['TRELLO_DONE_LIST_ID']

if "TRELLO_API_KEY" in os.environ:
    trello_apiKey=os.environ['TRELLO_API_KEY']

if "TRELLO_API_TOKEN" in os.environ:
    trello_apiToken=os.environ['TRELLO_API_TOKEN']
  
if "HABITICA_USERS_BY_TRELLO_MEMBER_ID" in os.environ:
    habitica_users_by_trello_member_id=json.loads(os.environ['HABITICA_USERS_BY_TRELLO_MEMBER_ID'])



