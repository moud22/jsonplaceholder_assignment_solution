import pytest
from comments.comment_endpoints import CommentEndPoints

# Comment Endpoints fixture
@pytest.fixture
def comment_endpoint():
    return CommentEndPoints

# Comment data for creation (unique data for each comment)
@pytest.fixture
def create_comment_data_fixture():
    post_id = 2  # Common post ID for all comments
    return [
        {
            "postId": post_id,
            "name": "First Comment",
            "email": "test1@example.com",
            "body": "This is the first comment body"
        },
        {
            "postId": post_id,
            "name": "Second Comment",
            "email": "test2@example.com",
            "body": "This is the second comment body"
        },
        {
            "postId": post_id,
            "name": "Third Comment",
            "email": "test3@example.com",
            "body": "This is the third comment body"
        }
    ]
