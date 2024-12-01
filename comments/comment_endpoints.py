from enum import Enum

class CommentEndPoints(Enum):
    get_all_comment_of_post = "/posts/{postId}/comments/"
    create_comment = "/posts/{postId}/comments/"
