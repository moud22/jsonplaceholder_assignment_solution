from enum import Enum

class PostEndPoints(Enum):
    get_all_post = "posts/"
    get_single_post = "posts/{id}/"
    create_post = "posts/"
    update_post = "posts/{id}/"
    delete_post = "posts/{id}/"