# How to run

## Attention
* Before running anything, please change the .env to suit your database setup
* After the .env file is appropriately changed, cd to the main directory of the repository, then:

### Use python 3.10+ to run
```
    # create a virtual environment specifically called fastmongo
    > python -m venv fastmongo

    # activating venv in windows
    > fastmongo\Scripts\Activate

    # install requirements
    > pip install -r requirements.txt

    # run development server
    > uvicorn main:app --reload

    # open the docs to test api calls
    > click the link presented in the console
```
