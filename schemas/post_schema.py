def individual_serial(post) -> dict:
    return {
        "_id": str(post["_id"]),
        "rocktype": (post["rocktype"]),
        "title": (post["title"]),
        "picture": (post["picture"]),
        "description": (post["description"]),
        "location": (post["location"]),
        "hashtags": (post["hashtags"]),
        "liked": (post["liked"]),
        "user_id": (post["user_id"]),
    }

def post_list_serial(posts) -> list:
    return[individual_serial(post) for post in posts]