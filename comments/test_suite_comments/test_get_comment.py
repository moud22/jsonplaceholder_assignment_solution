from comments.comment_endpoints import CommentEndPoints
from common_utils import rest_apis
from config.set_up import get_logger

log = get_logger()

def test_get_comments_of_valid_post():
    """
    Test get comments for valid post given a post id 
    """
    try:
        comment_list_response = rest_apis.send_get_request_with_id_comment(CommentEndPoints.get_all_comment_of_post.value, postId=2) # here id is post id
        response_code = comment_list_response.status_code

        comment_list = comment_list_response.json()

        assert response_code == 200
        for comment in comment_list:
            assert comment.get("postId"), "postId key is not valid"
            assert comment.get("id"), "id key is not valid"
            assert comment.get("name"), "title key is not valid"
            assert comment.get("email"), "email key is not valid"
            assert comment.get("body"), "body key is not valid"
    except Exception as e:
        log.error(f"Error while getting comments for valid post - {str(e)}")


    