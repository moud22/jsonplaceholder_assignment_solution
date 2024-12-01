from common_utils import rest_apis
from posts.posts_endpoint import PostEndPoints
from posts.test_suite_posts.fixtures.test_update_post_fixture import post_endpoint, update_post_data_fixture

def test_update_post(post_endpoint, update_post_data_fixture):
    id = 1  # Example post ID; can be dynamic based on your logic

    for update_data in update_post_data_fixture:  # Iterate over update data
        response = rest_apis.send_update_request(
            PostEndPoints.update_post.value,
            update_data,
            id
        )

        # Verify the response status code and updated data
        assert response.status_code == 200, f"Failed to update post with ID {id}"
        assert response.json().get("title") == update_data["title"], f"Expected title {update_data['title']}, got {response.json().get('title')}"
