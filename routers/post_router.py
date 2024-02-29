from fastapi import APIRouter
from schemas.post_schema import post_list_serial
from models.post_model import Post
from bson import ObjectId
from config.connection import db

router = APIRouter()
collection = db["post"]

# get all the post as a list
@router.get("/get_all_posts")
def get_all_posts():
    posts = post_list_serial(collection.find())
    return posts

# get a specific post based on the id
@router.get("/get_post/{id}")
def get_account(id: str):
    post = post_list_serial(collection.find({"_id": ObjectId(id)}))

    return post

# query post based on title
@router.get("/search_posts/")
def search_posts(title:str):
    posts = post_list_serial(collection.find({"title":{"$regex":title}}))
    return posts

# add new post to the database
@router.post("/add_post")
def add_post(post: Post):
    collection.insert_one(dict(post))

    return {"message": "post has been added succesfully"}

# modify a post (for admin idk)
@router.put("/modify_post/{id}")
def modify_post(id: str, post: Post):
    collection.find_one_and_update(
        {
            "_id": ObjectId(id)
        },
        {   
            "$set": dict(post)
        }
    )

    return {"message": "Post has been edited succesfully"}

# modify post's user id (poster)
@router.put("/edit_post_userid/{id}")
def edit_post_userid(id: str, user_id: str):
    post = collection.find_one({"_id": ObjectId(id)})
    post["user_id"] = user_id
    collection.find_one_and_update(
        {
            "_id": ObjectId(id)
        },
        {   
            "$set": dict(post)
        }
    )

    return {"message": "post's user_id (poster) has been changed"}

# modify post's rocktype
@router.put("/edit_post_rocktype/{id}")
def edit_post_rocktype(id: str, rocktype: str):
    post = collection.find_one({"_id": ObjectId(id)})
    post["rocktype"] = rocktype
    collection.find_one_and_update(
        {
            "_id": ObjectId(id)
        },
        {   
            "$set": dict(post)
        }
    )

    return {"message": "post's rocktype has been changed"}

# modify post's title
@router.put("/edit_post_title/{id}")
def edit_post_title(id: str, title: str):
    post = collection.find_one({"_id": ObjectId(id)})
    post["title"] = title
    collection.find_one_and_update(
        {
            "_id": ObjectId(id)
        },
        {   
            "$set": dict(post)
        }
    )

    return {"message": "post's title has been changed"}

# modify post's picture
@router.put("/edit_post_picture/{id}")
def edit_post_picture(id: str, picture: str):
    post = collection.find_one({"_id": ObjectId(id)})
    post["picture"] = picture
    collection.find_one_and_update(
        {
            "_id": ObjectId(id)
        },
        {   
            "$set": dict(post)
        }
    )

    return {"message": "post's picture has been changed"}

# modify post's description
@router.put("/edit_post_description/{id}")
def edit_post_description(id: str, description: str):
    post = collection.find_one({"_id": ObjectId(id)})
    post["description"] = description
    collection.find_one_and_update(
        {
            "_id": ObjectId(id)
        },
        {   
            "$set": dict(post)
        }
    )

    return {"message": "post's description has been changed"}

# modify post's location
@router.put("/edit_post_location/{id}")
def edit_post_location(id: str, location: list[float]):
    post = collection.find_one({"_id": ObjectId(id)})
    post["location"] = location
    collection.find_one_and_update(
        {
            "_id": ObjectId(id)
        },
        {   
            "$set": dict(post)
        }
    )

    return {"message": "post's location has been changed"}

# modify post's hashtags
@router.put("/edit_post_hashtags/{id}")
def edit_post_hashtags(id: str, hashtags: list[str]):
    post = collection.find_one({"_id": ObjectId(id)})
    post["hashtags"] = hashtags
    collection.find_one_and_update(
        {
            "_id": ObjectId(id)
        },
        {   
            "$set": dict(post)
        }
    )

    return {"message": "post's hashtags has been changed"}

# add new account ids to a specific post's liked field
@router.put("/add_account_to_post_liked/{id}")
def add_account_to_post_liked(id: str, account_ids: list[str]):
    post = collection.find_one({"_id": ObjectId(id)})
    original_liked = post.get('liked')
    for account_id in account_ids:
        original_liked.append(account_id)
    new_post = dict(post)
    collection.find_one_and_update(
        {
            "_id": ObjectId(id)
        },
        {   
            "$set": new_post
        }
    )

    return {"message": "account_id(s) has been added to the liked field succesfully"}

# remove account ids to a specific post's liked field
@router.put("/remove_account_from_post_liked/{id}")
def remove_account_from_post_liked(id: str, account_ids: list[str]):
    post = collection.find_one({"_id": ObjectId(id)})
    original_liked = post.get('liked')
    for account_id in account_ids:
        try:
            original_liked.remove(account_id)
        except:
            continue
    new_post = dict(post)
    collection.find_one_and_update(
        {
            "_id": ObjectId(id)
        },
        {   
            "$set": new_post
        }
    )

    return {"message": "account_id(s) has been removed from the liked field succesfully"}

# modify the liked field of the post collection
@router.put("/modify_post_liked/{id}")
def modify_post_liked(id: str, liked: list[str]):
    post = collection.find_one({"_id": ObjectId(id)})
    post["ilked"] = liked
    collection.find_one_and_update(
        {
            "_id": ObjectId(id)
        },
        {   
            "$set": dict(post)
        }
    )

    return {"message": "post's liked field has been modified succesfully"}

# delete a post (can be both for admin and user if they want to delete their post)
@router.delete("/delete_post/{id}")
def delete_post(id: str):
    collection.find_one_and_delete({"_id": ObjectId(id)})