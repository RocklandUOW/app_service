# serialize the collection from json file so its readable by python in a list form

def individual_serial(account) -> dict:
    return {
        "_id": str(account["_id"]),
        "email": (account["email"]),
        "username": (account["username"]),
        "password":(account["password"]),
        "posts": (account["posts"])
    }

def password_protected(account) -> dict:
    return {
        "_id": str(account["_id"]),
        "email": (account["email"]),
        "username": (account["username"]),
        "password": "*********",
        "posts": (account["posts"])
    }


def account_list_serial(accounts) -> list:
    return[individual_serial(account) for account in accounts]

def account_pass_prot_list_serial(accounts) -> list:
    return[password_protected(account) for account in accounts]