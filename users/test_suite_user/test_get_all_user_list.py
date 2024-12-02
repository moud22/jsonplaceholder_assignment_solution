from config.set_up import get_logger
from users.user_endpoints import UserEndPoints
from common_utils import rest_apis

log = get_logger()

def test_get_all_user_list():
    """
    test case method for getting the user list
    """
    try:
        user_list_response = rest_apis.send_get_request(UserEndPoints.get_all_user.value)
        response_code = user_list_response.status_code
        user_list = user_list_response.json()

        assert response_code == 200, "not getting user list"
        for user in user_list:
            assert user.get("name"), "name key is not valid"
            assert user.get("email"), "email key is not valid"
            assert user.get("address"), "address key is not valid"
    except Exception as e:
        log.error(f"Error while fetching list of users -{str(e)}")

    