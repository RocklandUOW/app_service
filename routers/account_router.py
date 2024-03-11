from fastapi import APIRouter
from schemas.account_schema import account_list_serial, account_pass_prot_list_serial
from models.account_model import Account
from models.model_schemas import PassCheck
from bson import ObjectId
from config.connection import db

router = APIRouter()
collection = db["account"]

# get all the accounts as a list
@router.get("/get_all_accounts")
def get_all_accounts():
    accounts = account_pass_prot_list_serial(collection.find())
    return accounts

# get a specific account based on the id
@router.get("/get_account/{id}")
def get_account(id: str):
    account = account_pass_prot_list_serial(collection.find({"_id": ObjectId(id)}))

    return account

# query account based on username
@router.get("/search_accounts/")
def search_account(username:str):
    accounts = account_pass_prot_list_serial(collection.find({"username":{"$regex":username}}))
    return accounts

# check for password for given account
@router.post("/check_password/")
def search_account(form: PassCheck):
    form = dict(form)
    account = collection.find_one({"username":form.get("username")})
    
    try:
        checkValue = (account.get("password") == form.get("password"))
    except:
        return {"message": "account not found"}

    if (checkValue):
        return {"message": "match"}
    else:
        return {"message": "hacker"}

# add new account to the database
@router.post("/add_account")
def add_account(account: Account):
    collection.insert_one(dict(account))

    return {"message": "Account has been added succesfully"}

# modify an account (for admin maybe idk)
@router.put("/modify_account/{id}")
def modify_account(id: str, account: Account):
    collection.find_one_and_update(
        {
            "_id": ObjectId(id)
        },
        {   
            "$set": dict(account)
        }
    )

    return {"message": "Account has been edited succesfully"}

# edit account email
@router.put("/edit_account_email/{id}")
def edit_account_email(id: str, email: str):
    account = collection.find_one({"_id": ObjectId(id)})
    account["email"] = email
    collection.find_one_and_update(
        {
            "_id": ObjectId(id)
        },
        {   
            "$set": dict(account)
        }
    )

    return {"message": "account email has been changed"}

# edit account username
@router.put("/edit_account_username/{id}")
def edit_account_username(id: str, username: str):
    account = collection.find_one({"_id": ObjectId(id)})
    account["username"] = username
    collection.find_one_and_update(
        {
            "_id": ObjectId(id)
        },
        {   
            "$set": dict(account)
        }
    )

    return {"message": "account username has been changed"}

# edit account password
@router.put("/edit_account_password/{id}")
def edit_account_password(id: str, password: str):
    account = collection.find_one({"_id": ObjectId(id)})
    account["password"] = password
    collection.find_one_and_update(
        {
            "_id": ObjectId(id)
        },
        {   
            "$set": dict(account)
        }
    )

    return {"message": "account password has been changed"}

# add new post to a specific account
@router.put("/add_post_to_account/{id}")
def add_post_to_account(id: str, posts: list[str]):
    account = collection.find_one({"_id": ObjectId(id)})
    original_posts = account.get('posts')
    for post in posts:
        original_posts.append(post)
    new_account = dict(account)
    collection.find_one_and_update(
        {
            "_id": ObjectId(id)
        },
        {   
            "$set": new_account
        }
    )

    return {"message": "post(s) has been added to the account succesfully"}

# remove a post from a specific account
@router.put("/remove_post_from_account/{id}")
def remove_post_from_account(id: str, posts: list[str]):
    account = collection.find_one({"_id": ObjectId(id)})
    original_posts = account.get('posts')
    for post in posts:
        try:
            original_posts.remove(post)
        except:
            continue
    new_account = dict(account)
    collection.find_one_and_update(
        {
            "_id": ObjectId(id)
        },
        {   
            "$set": new_account
        }
    )

    return {"message": "post(s) has been removed from the account succesfully"}

# modify the post of an account
@router.put("/modify_account_posts/{id}")
def modify_account_posts(id: str, posts: list[str]):
    account = collection.find_one({"_id": ObjectId(id)})
    account["posts"] = posts
    collection.find_one_and_update(
        {
            "_id": ObjectId(id)
        },
        {   
            "$set": dict(account)
        }
    )

    return {"message": "account posts has been modified"}

# delete an account (can be both for admin and user if they want to delete their account)
@router.delete("/delete_account/{id}")
def delete_account(id: str):
    collection.find_one_and_delete({"_id": ObjectId(id)})