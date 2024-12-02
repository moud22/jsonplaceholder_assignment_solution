from common_utils import rest_apis
from config.set_up import get_logger
from posts.posts_endpoint import PostEndPoints

log = get_logger()

def test_get_single_post_valid_id():
    """
    test case method to get single post with valid id
    """
    try:
        post_response = rest_apis.send_get_request_with_id(PostEndPoints.get_single_post.value, id=2) # here id is post_id
        response_code = post_response.status_code

        assert response_code == 200
        assert post_response.json()["userId"] == 1
        assert post_response.json()["id"] == 2
        assert post_response.json()["title"] == "qui est esse"
        assert post_response.json()["body"] == "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
    except Exception as e:
        log.error(f"Error while validating single post id {str(e)}")

def test_get_single_post_invalid_id():
    """
    test case method to get single post with invalid id
    """
    try:
        post_response = rest_apis.send_get_request_with_id(PostEndPoints.get_single_post.value, id=2000) # here id is post_id
        response_code = post_response.status_code

        assert response_code == 404
    except Exception as e:
        log.error(f"Error while getting single post for invalid id {str(e)}")


    