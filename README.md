# Integrate Trello with Habitica

Finish tasks on Trello and they automatically get scored on Habitica when you run the program.

1.  Fill the user_details.py file with the api keys and tokens for habitica and trello. Create a list where you put
    all of your "done" tasks, and get its id. Program will take the cards from the "done" list and score them on habitica.

        * Expected format for habitica_users_by_trello_member_id:
        ```
        {
            "35345jjkjkhjkhkk345k4j5h": { // memberId from trello
                "name": "captainawesome",
                "habitica_user_key": "34j5hkjh-3456-kkj5-4567-jkj4fgdf5656",
                "habitica_api_token": "34j5hkjh-3456-kkj5-4567-jkj4fgdf5656"
            },
            "35345jjkjkhjkhkk345k4j5g": { // memberId from trello
                "name": "almostasawesomeasthecaptain",
                "habitica_user_key": "34j5hkjh-3456-kkj5-4567-jkj4fgdf5656",
                "habitica_api_token": "34j5hkjh-3456-kkj5-4567-jkj4fgdf5656"
            }
        }
        ```

2.  Decide on the date, from which point you want to start pushing things that are done in Trello to Habitica.
    If the date is not specified, program will choose the date the list was first created.
    You can select a date, and write it in this format in the file \_date_run_last.txt:
    Format: '%Y-%m-%dT%H-%M-%S'. Example: 2018-07-21T21-33-45, no spaces.

3.  You can select difficulty level of a task either by putting in 1 to 4 stars in increasing order for increasing difficulty
    or by writing the difficulty level in brackets in the card name. i.e [trivial], [easy], [medium], [hard].
    Otherwise, task is created as easy by default. Example: "Send email to Johnathan \*\*"

## Usage (docker)

[Docker Repositoy](https://hub.docker.com/r/andersonxbs/trello-habitica-integration/)

### Environment Variables

#### PROCESS_INTERVAL_IN_SECONDS (Optional)

Interval in seconds for checking for new done tasks on trello. Default is 3600 seconds (1 hour)

#### START_DATE (Optional)

Datetime to start looking for tasks on done list.
Format: '%Y-%m-%dT%H-%M-%S'. Example: 2018-07-21T21-33-45, no spaces.
If not set, it will look for tasks since the list was first created.

#### TRELLO_DONE_LIST_ID

Id of your list of done tasks on trello.

#### TRELLO_API_KEY

Your trello API keys.

#### TRELLO_API_TOKEN

Your trello API token.

#### HABITICA_USERS_BY_TRELLO_MEMBER_ID

It must have API keys and API tokens of the users on Habitica acording to the member id of trello.
Example:

```json
{
  "35345jjkjkhjkhkk345k4j5h": {
    "name": "captainawesome",
    "habitica_user_key": "34j5hkjh-3456-kkj5-4567-jkj4fgdf5656",
    "habitica_api_token": "34j5hkjh-3456-kkj5-4567-jkj4fgdf5656"
  },
  "35345jjkjkhjkhkk345k4j5g": {
    "name": "almostasawesomeasthecaptain",
    "habitica_user_key": "34j5hkjh-3456-kkj5-4567-jkj4fgdf5656",
    "habitica_api_token": "34j5hkjh-3456-kkj5-4567-jkj4fgdf5656"
  }
}
```

In this example, 35345jjkjkhjkhkk345k4j5h and 35345jjkjkhjkhkk345k4j5g are the memberIds values from trello.

## Docker Compose

Example with fake values:

```docker-compose
version: '3'

services:
  trello-s2-habitica:
    container_name: trello-s2-habitica
    image: andersonxbs/trello-habitica-integration
    volumes:
     - "./docker-volume:/usr/src/app/data"
    environment:
      PROCESS_INTERVAL_IN_SECONDS: 60
      START_DATE: '2018-08-16T08-00-00'
      TRELLO_DONE_LIST_ID: 'sakjdfkjs8d7f8a7sd8f7asdjfh8'
      TRELLO_API_KEY: 'kjskljdf8asd8f098s9d8f98asdfisjdf0s8df'
      TRELLO_API_TOKEN: 'ajsdkfjkljasdf9078a908s7dfjahsdf90a7sdjfha908sdfjkahsdf987jhsd9'
      HABITICA_USERS_BY_TRELLO_MEMBER_ID: >
        {
          "35345jjkjkhjkhkk345k4j5h": {
            "name": "captainawesome",
            "habitica_user_key": "34j5hkjh-3456-kkj5-4567-jkj4fgdf5656",
            "habitica_api_token": "34j5hkjh-3456-kkj5-4567-jkj4fgdf5656"
          },
          "35345jjkjkhjkhkk345k4j5g": {
            "name": "almostasawesomeasthecaptain",
            "habitica_user_key": "34j5hkjh-3456-kkj5-4567-jkj4fgdf5656",
            "habitica_api_token": "34j5hkjh-3456-kkj5-4567-jkj4fgdf5656"
          }
        }
```
