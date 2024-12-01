import pytest
from posts.posts_endpoint import PostEndPoints

# Post Endpoints fixture
@pytest.fixture
def post_endpoint():
    return PostEndPoints

# Post data for updating (parameterized for multiple sets of data)
@pytest.fixture
def update_post_data_fixture():
    return [
        {
            "userId": 1,
            "title": "Updated First Post Title",
            "body": "Updated First Post Body"
        },
        {
            "userId": 2,
            "title": "Updated Second Post Title",
            "body": "Updated Second Post Body"
        },
        {
            "userId": 3,
            "title": "Updated Third Post Title",
            "body": "Updated Third Post Body"
        }
    ]
