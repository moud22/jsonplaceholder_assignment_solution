from users_module.user_payloads import user_payload
from users_module.user_endpoints import UserEndPoints
from config.set_up import *
from common_utils import rest_apis

def test_get_all_user_list():
    user_list_response = rest_apis.send_get_request(UserEndPoints.get_all_user.value)
    response_code = user_list_response.status_code

    user_list = user_list_response.json()

    for user in user_list:
        assert user.get("name"), "name key is not valid"
        assert user.get("email"), "email key is not valid"
        assert user.get("address"), "address key is not valid"

    