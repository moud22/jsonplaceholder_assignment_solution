import jsonschema
import requests
from config.set_up import base_url

# GET API calls for list retrieval for user and post
def send_get_request(endpoint):
    get_response = requests.get(base_url + endpoint)
    assert get_response.elapsed.total_seconds() < 10, "API Call is taking longer time"
    return get_response

# GET API call for indivdual data retrieval for users, posts and comments
def send_get_request_with_id(endpoint, id):
    get_response = requests.get(base_url + endpoint.format(id=id))
    assert get_response.elapsed.total_seconds() < 10, "API Call is taking longer time"
    return get_response

# GET API call for indivdual data retrieval comments
def send_get_request_with_id_comment(endpoint, postId):
    get_response = requests.get(base_url + endpoint.format(postId=postId))
    assert get_response.elapsed.total_seconds() < 10, "API Call is taking longer time"
    return get_response

# POST API call for new record creation for user, post, comments
def send_post_request(endpoint, payloads):
    post_response = requests.post(base_url + endpoint, json=payloads)
    assert post_response.elapsed.total_seconds() < 10,  "API Call is taking longer time"
    return post_response

# POST API call for new record creation comments
def send_post_request_comment(endpoint, postId, payloads):
    post_response = requests.post(base_url + endpoint.format(postId=postId), json=payloads)
    assert post_response.elapsed.total_seconds() < 10,  "API Call is taking longer time"
    return post_response

# UPDATE API call using PUT method for updating resources for user
def send_update_request(endpoint, payloads, id):
    put_response = requests.put(base_url + endpoint.format(id=id), json=payloads)
    assert put_response.elapsed.total_seconds() < 10, "API Call is taking longer time"
    return put_response

# DELETE API call for user
def send_delete_request(endpoint, id):
    delete_response = requests.delete(base_url + endpoint.format(id=id))
    return delete_response

