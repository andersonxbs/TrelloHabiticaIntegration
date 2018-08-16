# Integrate Trello with Habitica
Finish tasks on Trello and they automatically get scored on Habitica when you run the program.

1. Fill the user_details.py file with the api keys and tokens for habitica and trello. Create a list where you put
all of your "done" tasks, and get its id. Program will take the cards from the "done" list and score them on habitica.

    * Expected format for habitica_users_by_trello_member_id:
    ```
    {
        "35345jjkjkhjkhkk345k4j5h": { // mamberId from trello
            "name": "captainawesome",
            "habitica_user_key": "34j5hkjh-3456-kkj5-4567-jkj4fgdf5656",
            "habitica_api_token": "34j5hkjh-3456-kkj5-4567-jkj4fgdf5656"
        },
        "35345jjkjkhjkhkk345k4j5g": { // mamberId from trello
            "name": "almostasawesomeasthecaptain",
            "habitica_user_key": "34j5hkjh-3456-kkj5-4567-jkj4fgdf5656",
            "habitica_api_token": "34j5hkjh-3456-kkj5-4567-jkj4fgdf5656"
        }
    }
    ```

2. Decide on the date, from which point you want to start pushing things that are done in Trello to Habitica.
If the date is not specified, program will choose the date the list was first created.
You can select a date, and write it in this format in the file _date_run_last.txt:
Format: '%Y-%m-%dT%H-%M-%S'. Example: 2018-07-21T21-33-45, no spaces.

3. You can select difficulty level of a task either by putting in 1 to 4 stars in increasing order for increasing difficulty
or by writing the difficulty level in brackets in the card name. i.e (hard), (easy), (medium), (trivial).
Otherwise, task is created as easy by default. Example: "Send email to Johnathan **"

# Links
[Docker Repositoy](https://hub.docker.com/r/andersonxbs/trello-s2-habitica/)
