from config.set_up import get_logger
from users.user_endpoints import UserEndPoints
from common_utils import rest_apis

log = get_logger()

def test_get_single_user_valid_id():
    """
    test case method for getting asingle user based on valid and existing id
    """
    try:
        user_response = rest_apis.send_get_request_with_id(UserEndPoints.get_single_user.value, id=2) # here id is user_id
        response_code = user_response.status_code

        assert response_code == 200, "failed to get the user"
        assert user_response.json()["name"] == "Ervin Howell"
        assert user_response.json()["email"] == "Shanna@melissa.tv"
        assert user_response.json()["address"]["city"] == "Wisokyburgh"
    except Exception as e:
        log.error(f"Error while validating single user id {str(e)}")

def test_get_single_user_invalid_id():
    """
    test case method for getting asingle user based on valid but non-existing id
    """
    try:
        user_response = rest_apis.send_get_request_with_id(UserEndPoints.get_single_user.value, id=2000) # here id is user_id
        response_code = user_response.status_code

        assert response_code == 404
    except Exception as e:
        log.error(f"Error while validating single user invalid id {str(e)}")


    