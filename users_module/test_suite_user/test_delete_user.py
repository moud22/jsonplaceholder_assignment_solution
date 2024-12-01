from users_module.user_payloads import user_payload
from users_module.user_endpoints import UserEndPoints
from users_module.user_payloads.user_payload import *
from config.set_up import *
from common_utils import rest_apis

def test_delete_single_user():
    deletion_response = rest_apis.send_delete_request(UserEndPoints.delete_single_user.value, user_id=11)
    assert deletion_response.status_code == 200

    #subsequentget call to verify if user has been deleted or not
    deleted_user_response = rest_apis.send_get_request_with_id(UserEndPoints.get_single_user.value, user_id=11)
    assert deleted_user_response.status_code == 404