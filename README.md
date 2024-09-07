# Chat Application

This is a group chat application made with Django.

Deployed on Render: [Website][1]

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
    poetry run python3 manage.py runserver

## Local deployement
To deploy locally for test:

    daphne group_chat.asgi:application

## Project description
### Files
- `build.sh`: build script used by Render to deploy

## Feedback and Issues
Feel free to raise issues or to provide any feeback.
Any contribution are welcome!

Take a look at:
- [Current issues](https://github.com/HarimbolaSantatra/django-group-chat/issues)
- [TODO list](todo.md)

[1]: https://group-chat-s9wl.onrender.com
