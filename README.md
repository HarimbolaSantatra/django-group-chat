# Chat Application

This is a group chat application made with Django, deployed [on Render][1].

### Screenshot:
![screenshot](screenshot.png)

## Local development
[Install poetry](https://python-poetry.org/docs/) (this example use a virtual environment:

    VENV_PATH=/home/$USER/.python-venv/poetry
    mkdir -p $VENV_PATH
    python3 -m venv $VENV_PATH
    $VENV_PATH/bin/pip install -U pip setuptools
    $VENV_PATH/bin/pip install poetry
    source $VENV_PATH/bin/activate

and run:

    poetry install

To deploy locally for test, run one of these commands (the first format is *recommended* because it's the one the project is using on production:

    daphne group_chat.asgi:application
    poetry run python3 manage.py runserver

## Project description
### Files
- `build.sh`: build script used by Render to deploy
- `data.json`: the flat file database

### Branch
- *legacy-no-ws*: using simple JS script + file writing to update the UI and the database, without using websocket
- *master*: production

## Feedback and Issues
Feel free to raise issues or to provide any feeback.
Any contribution are welcome!

Take a look at the [current issues](https://github.com/HarimbolaSantatra/django-group-chat/issues).

[1]: https://group-chat-s9wl.onrender.com
