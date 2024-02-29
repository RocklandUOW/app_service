from fastapi import APIRouter, Path, Query
from schemas.account_schema import list_serial, pass_prot_list_serial
from models.account_model import Account
from typing import Annotated
from bson import ObjectId
from config.connection import db

router = APIRouter()
collection = db["account"]

# get all the accounts as a list
@router.get("/get_all_accounts")
def get_all_accounts():
    accounts = pass_prot_list_serial(collection.find())
    return accounts

# get a specific account based on the id
@router.get("/get_account/{id}")
def get_account(id: str):
    account = pass_prot_list_serial(collection.find({"_id": ObjectId(id)}))

    return account

# query account based on username
@router.get("/search_accounts/")
def search_account(username:str):
    accounts = pass_prot_list_serial(collection.find({"username":{"$regex":username}}))
    return accounts

# add new account to the database
@router.post("/add_account")
def add_account(account: Account):
    collection.insert_one(dict(account))

    return {"message": "Account has been added succesfully"}

# modify an account (for admin maybe idk)
@router.put("/edit_account/{id}")
def edit_account(id: str, account: Account):
    collection.find_one_and_update(
        {
            "_id": ObjectId(id)
        },
        {   
            "$set": dict(account)
        }
    )

    return {"message": "Account has been edited succesfully"}

# delete an account (can be both for admin and user if they want to delete their account)
@router.delete("/delete_account/{id}")
def delete_account(id: str):
    collection.find_one_and_delete({"_id": ObjectId(id)})

# add new post to a specific account
@router.put("/add_post/{id}")
def add_post_to_account(id: str, posts: list[int]):
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
@router.put("/remove_post/{id}")
def remove_post_from_account(id: str, posts: list[int]):
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