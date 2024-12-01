import pytest
from users_module.user_endpoints import UserEndPoints

# User Endpoints fixture
@pytest.fixture
def user_endpoint():
    return UserEndPoints

# User data for creation (parameterized for multiple sets of data)
@pytest.fixture
def user_data_fixture():
    return [
        {
            "name": "John Doe",
            "username": "johndoe1",
            "email": "johndoe1@example.com",
            "address": {
                "street": "123 Main St",
                "suite": "Apt. 1",
                "city": "City A",
                "zipcode": "12345",
                "geo": {"lat": "12.34", "lng": "56.78"}
            },
            "phone": "1-555-555-5551",
            "website": "johndoe1.com",
            "company": {"name": "Company A", "catchPhrase": "Innovation at scale", "bs": "tech"}
        },
        {
            "name": "Jane Smith",
            "username": "janesmith2",
            "email": "janesmith2@example.com",
            "address": {
                "street": "456 Elm St",
                "suite": "Apt. 2",
                "city": "City B",
                "zipcode": "67890",
                "geo": {"lat": "23.45", "lng": "67.89"}
            },
            "phone": "1-555-555-5552",
            "website": "janesmith2.com",
            "company": {"name": "Company B", "catchPhrase": "Leading the future", "bs": "business"}
        },
        {
            "name": "Alice Johnson",
            "username": "alicejohnson3",
            "email": "alicejohnson3@example.com",
            "address": {
                "street": "789 Oak St",
                "suite": "Apt. 3",
                "city": "City C",
                "zipcode": "11223",
                "geo": {"lat": "34.56", "lng": "78.90"}
            },
            "phone": "1-555-555-5553",
            "website": "alicejohnson3.com",
            "company": {"name": "Company C", "catchPhrase": "The future of tech", "bs": "engineering"}
        }
    ]
