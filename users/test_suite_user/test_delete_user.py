from users.user_endpoints import UserEndPoints
from config.set_up import *
from common_utils import rest_apis

log = get_logger()

def test_delete_single_user():
    """
    test case method for deleting an user
    """
    try:
        deletion_response = rest_apis.send_delete_request(UserEndPoints.delete_single_user.value, id=11)
        assert deletion_response.status_code == 200

        # subsequentget call to verify if user has been deleted or not
        deleted_user_response = rest_apis.send_get_request_with_id(UserEndPoints.get_single_user.value, id=11)
        assert deleted_user_response.status_code == 404
    except Exception as e:
        log.error(f"Error while deleting single user - {str(e)}")