from common_utils import rest_apis
from comments.test_suite_comments.test_create_comment_fixture import comment_endpoint, create_comment_data_fixture
from config.set_up import get_logger

log = get_logger()

def test_create_comment_of_valid_post(comment_endpoint, create_comment_data_fixture):
    """ 
    creating a comment for a valid post 
    """
    try:
        for comment_data in create_comment_data_fixture:  # Iterate over comment data
            response = rest_apis.send_post_request_comment(
                comment_endpoint.create_comment.value,  # Endpoint for creating comments
                postId=comment_data["postId"],  # Post ID from the fixture file
                payloads=comment_data
            )

            assert response.status_code == 201, "Failed to create comment"
            assert response.json().get("id"), "Comment ID not returned in response"
    except Exception as e:
        log.error(f"error while creating comments for a valid post - {str(e)}")
