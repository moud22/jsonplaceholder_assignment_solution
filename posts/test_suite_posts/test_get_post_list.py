from posts.post_payloads import *
from posts.posts_endpoint import PostEndPoints
from config.set_up import *
from common_utils import rest_apis

def test_get_all_post_list():
    post_list_response = rest_apis.send_get_request(PostEndPoints.get_all_post.value)
    response_code = post_list_response.status_code

    post_list = post_list_response.json()

    for post in post_list:
        assert post.get("userId"), "user_id key is not valid"
        assert post.get("id"), "id key is not valid"
        assert post.get("title"), "title key is not valid"
        assert post.get("body"), "body key is not valid"