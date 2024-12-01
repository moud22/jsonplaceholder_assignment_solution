import pytest
from common_utils import rest_apis

# Import the fixture for user creation
from users_module.test_suite_user.fixtures.test_create_user_fixtures import user_data_fixture, user_endpoint

def test_create_user(user_endpoint, user_data_fixture):
    for user_data in user_data_fixture:  # Iterate over user data in the fixture
        response = rest_apis.send_post_request(
            user_endpoint.create_user.value,
            user_data
        )
        
        # Verify the response status code and if the user id exists
        assert response.status_code == 201
        assert response.json().get("id"), "id key didn't return"
