from common_utils import rest_apis
from posts.posts_endpoint import PostEndPoints
from posts.test_suite_posts.fixtures.test_create_post_fixture import post_endpoint, create_post_data_fixture

def test_create_post(post_endpoint, create_post_data_fixture):
    for post_data in create_post_data_fixture:  # Iterate over post data
        response = rest_apis.send_post_request(
            post_endpoint.create_post.value,  # 'posts/' endpoint
            post_data
        )

        # Verify the response status code and if the post was created successfully
        assert response.status_code == 201, "Failed to create post"
        assert response.json().get("id"), "Post ID not returned in response"
