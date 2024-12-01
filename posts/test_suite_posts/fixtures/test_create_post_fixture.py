import pytest
from posts.posts_endpoint import PostEndPoints

# Post Endpoints fixture
@pytest.fixture
def post_endpoint():
    return PostEndPoints

# Post data for creation (parameterized for multiple sets of data)
@pytest.fixture
def create_post_data_fixture():
    return [
        {
            "userId": 1,
            "title": "First Post Title",
            "body": "First Post Body"
        },
        {
            "userId": 2,
            "title": "Second Post Title",
            "body": "Second Post Body"
        },
        {
            "userId": 3,
            "title": "Third Post Title",
            "body": "Third Post Body"
        }
    ]
