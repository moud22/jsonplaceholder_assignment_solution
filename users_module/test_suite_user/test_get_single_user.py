from users_module.user_payloads import user_payload
from users_module.user_endpoints import UserEndPoints
from config.set_up import *
from common_utils import rest_apis

def test_get_single_user_valid_id():
    user_response = rest_apis.send_get_request_with_id(UserEndPoints.get_single_user.value, id=2) # here id is user_id
    response_code = user_response.status_code

    assert response_code == 200
    assert user_response.json()["name"] == "Ervin Howell"
    assert user_response.json()["email"] == "Shanna@melissa.tv"
    assert user_response.json()["address"]["city"] == "Wisokyburgh"

def test_get_single_user_invalid_id():
    user_response = rest_apis.send_get_request_with_id(UserEndPoints.get_single_user.value, id=2000) # here id is user_id
    response_code = user_response.status_code

    assert response_code == 404


    