import requests
from config.set_up import base_url

def send_get_request(endpoint):
    """
    GET API calls for list retrieval for user and post
    """
    get_response = requests.get(base_url + endpoint)
    assert get_response.elapsed.total_seconds() < 10, "API Call is taking longer time"
    return get_response

def send_get_request_with_id(endpoint, id):
    """
    GET API call for indivdual data retrieval for users and posts
    """
    get_response = requests.get(base_url + endpoint.format(id=id))
    assert get_response.elapsed.total_seconds() < 10, "API Call is taking longer time"
    return get_response

def send_get_request_with_id_comment(endpoint, postId):
    """
    GET API call for indivdual data retrieval comments
    """
    get_response = requests.get(base_url + endpoint.format(postId=postId))
    assert get_response.elapsed.total_seconds() < 10, "API Call is taking longer time"
    return get_response

def send_post_request(endpoint, payloads):
    """
    POST API call for new record creation for user and post
    """
    post_response = requests.post(base_url + endpoint, json=payloads)
    assert post_response.elapsed.total_seconds() < 10,  "API Call is taking longer time"
    return post_response

def send_post_request_comment(endpoint, postId, payloads):
    """
    POST API call for new record creation comments
    """
    post_response = requests.post(base_url + endpoint.format(postId=postId), json=payloads)
    assert post_response.elapsed.total_seconds() < 10,  "API Call is taking longer time"
    return post_response

def send_update_request(endpoint, payloads, id):
    """
    UPDATE API call using PUT method for updating resources for user
    """
    put_response = requests.put(base_url + endpoint.format(id=id), json=payloads)
    assert put_response.elapsed.total_seconds() < 10, "API Call is taking longer time"
    return put_response

def send_delete_request(endpoint, id):
    """
    DELETE API call for user
    """
    delete_response = requests.delete(base_url + endpoint.format(id=id))
    assert delete_response.elapsed.total_seconds() < 10, "API Call is taking longer time"
    return delete_response

