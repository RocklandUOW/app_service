# serialize the collection from json file so its readable by python in a list form

def individual_serial(account) -> dict:
    return {
        "email": (account["email"]),
        "username": (account["username"]),
        "password":(account["password"]),
        "posts": (account["posts"])
    }

def list_serial(accounts) -> list:
    return[individual_serial(account) for account in accounts]