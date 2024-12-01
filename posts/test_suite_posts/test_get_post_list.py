from common_utils import rest_apis
from config.set_up import get_logger
from posts.posts_endpoint import PostEndPoints

log = get_logger()

def test_get_all_post_list():
    try:
        post_list_response = rest_apis.send_get_request(PostEndPoints.get_all_post.value)
        response_code = post_list_response.status_code

        post_list = post_list_response.json()

        for post in post_list:
            assert post.get("userId"), "user_id key is not valid"
            assert post.get("id"), "id key is not valid"
            assert post.get("title"), "title key is not valid"
            assert post.get("body"), "body key is not valid"
    except Exception as e:
        log.error(f"Error while getting all post {str(e)}")