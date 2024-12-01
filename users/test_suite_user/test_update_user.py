from common_utils import rest_apis
from config.set_up import get_logger
from users.user_endpoints import UserEndPoints
from users.test_suite_user.fixtures.test_update_user_fixtures import update_user_data_fixture, user_endpoint

log = get_logger()

def test_update_user(user_endpoint, update_user_data_fixture):
    """
    Iterate over the user data and update each user using the data
    """
    try:
        user_id = 1  # Example user ID, you can modify it as needed or dynamically retrieve IDs

        for update_data in update_user_data_fixture:  # Iterate over each set of update data
            response = rest_apis.send_update_request(
                user_endpoint.update_single_user.value,  # 'users/{id}/' is fetched from the enum
                update_data,
                user_id
            )

            # Verify the response status code and updated data
            assert response.status_code == 200
            assert response.json().get("name") == update_data["name"], f"Expected {update_data['name']}, got {response.json().get('name')}"
            assert response.json().get("email") == update_data["email"], f"Expected {update_data['email']}, got {response.json().get('email')}"
        
    except Exception as e:
        log.error(f"Error while updating user {str(e)}")
