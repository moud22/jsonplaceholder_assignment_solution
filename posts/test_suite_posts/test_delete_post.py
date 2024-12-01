from posts.posts_endpoint import PostEndPoints
from config.set_up import *
from common_utils import rest_apis

def test_delete_single_post():
    deletion_response = rest_apis.send_delete_request(PostEndPoints.delete_post.value, id=501)
    assert deletion_response.status_code == 200

    #subsequentget call to verify if user has been deleted or not
    deleted_user_response = rest_apis.send_get_request_with_id(PostEndPoints.get_single_post.value, id=501)
    assert deleted_user_response.status_code == 404