##########################
############################
# Append today's date if all integration was successful to the file
# https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module
# https://stackoverflow.com/questions/47144606/requests-how-to-tell-if-youre-getting-a-success-message
'''
try:
 self.raise_for_status()
except requests.exceptions.RequestException as e:
  return False
'''
###########################
############################
import datetime
from time import sleep
import os

import trelloPart as tp
import habiticaPart as hp
import user_details as ud

def send_from_trello_to_habitica():
  print("Looking for new tasks [" + str(datetime.datetime.now()) + "]")
  # get the list of dictionaries each representing an action that took place in the list
  jsonList = tp.get_response_as_jsonList(ud.idOfList, ud.trello_apiKey, ud.trello_apiToken)
  # get only the valid cards that have been finished since the last time app was ran.
  validJsonElements = tp.get_done_cards_json(jsonList, ud.idOfList)
  # send each card
  counter = 0
  while counter<len(validJsonElements):
    jsonElement = validJsonElements[counter]
    cardJson = tp.get_card_as_json(jsonElement.get("data").get("card").get("id"), ud.trello_apiKey, ud.trello_apiToken) 
    priority = tp.find_difficulty_level(cardJson.get("name"))

    # try get assigned members of card
    idOfMembers = cardJson.get("idMembers")
    if (len(idOfMembers) == 0):
      # consider the member creator of the card for receiveing the scores if there is no one assigned
      idOfMembers.append(jsonElement.get("idMemberCreator"))

    for idMember in idOfMembers:   
      if idMember in ud.habitica_users_by_trello_member_id:
        f = open('data/test.json', 'a+')  # open file to read
        f.write(str(ud.habitica_users_by_trello_member_id))
        f.close()
        habiticaUser = ud.habitica_users_by_trello_member_id[idMember]
        (create_task_status_code, score_task_status_code) = hp.create_and_score_task(habiticaUser["habitica_user_key"], habiticaUser["habitica_api_token"], cardJson, priority)
        print("New task sent to habitica for user " + habiticaUser["name"] + " with create_tast_status_code " + str(create_task_status_code) + " and score_task_status_code " + str(score_task_status_code))

    counter += 1

  # if at least one card was sent and scored on habitica, log the date, so that next time
  # app will only take cards after this date.
  if(len(validJsonElements) > 0):
    # log the date
    f = open('data/_date_run_last.txt', 'a+')  # open file to read
    # write the current date
    fmt = '%Y-%m-%dT%H-%M-%S'
    ## get time now in UTC time
    now = datetime.datetime.utcnow()
    date_now=now.strftime(fmt) + "\n"
    f.write(date_now)
    f.close()

interval=3600
if "PROCESS_INTERVAL_IN_SECONDS" in os.environ:
    interval=int(os.environ['PROCESS_INTERVAL_IN_SECONDS'])

while True:
  send_from_trello_to_habitica()
  print("Checking again in " + str(interval) + " seconds")
  sleep(interval)

