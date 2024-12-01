from enum import Enum

class UserEndPoints(Enum):
    get_all_user = "users/"
    get_single_user = "users/{id}/"
    create_user = "users/"
    update_single_user = "users/{id}/"
    delete_single_user = "users/{id}/"
