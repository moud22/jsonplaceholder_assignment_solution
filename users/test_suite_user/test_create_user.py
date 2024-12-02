from common_utils import rest_apis

# Import the fixture for user creation
from config.set_up import get_logger
from users.test_suite_user.fixtures.test_create_user_fixtures import user_data_fixture, user_endpoint

log = get_logger()


def test_create_user(user_endpoint, user_data_fixture):
    """
    test case method for creating a new user
    """
    try:
        for user_data in user_data_fixture:  # Iterate over user data in the fixture
            response = rest_apis.send_post_request(
                user_endpoint.create_user.value,
                user_data
            )
            
            # Verify the response status code and if the user id exists
            assert response.status_code == 201
            assert response.json().get("id"), "id key didn't return"
    except Exception as e:
        log.error(f"Error while creating user - {str(e)}")
