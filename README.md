# How to run
Use python 3.10+ to run
```
    # After cloning the github repository, cd into directory
    # create a virtual environment specifically caled fastmongo
    > python -m venv fastmongo
    # activating venv in windows
    > fastmongo\Scripts\Activate
    # install requirements
    > pip install -r requirements.txt
    # run development server
    > uvicorn main:app --reload
    # access the docs to test api calls
    > go to http://127.0.0.1:8000/docs and use the methods presented
```
