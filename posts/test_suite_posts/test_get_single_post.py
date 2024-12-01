from posts.post_payloads import *
from posts.posts_endpoint import PostEndPoints
from config.set_up import *
from common_utils import rest_apis

def test_get_single_post_valid_id():
    post_response = rest_apis.send_get_request_with_id(PostEndPoints.get_single_post.value, id=2) # here id is post_id
    response_code = post_response.status_code

    assert response_code == 200
    assert post_response.json()["userId"] == 1
    assert post_response.json()["id"] == 2
    assert post_response.json()["title"] == "qui est esse"
    assert post_response.json()["body"] == "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"

def test_get_single_post_invalid_id():
    post_response = rest_apis.send_get_request_with_id(PostEndPoints.get_single_post.value, id=2000) # here id is post_id
    response_code = post_response.status_code

    assert response_code == 404


    