import pytest
from users.user_endpoints import UserEndPoints

# User Endpoints fixture
@pytest.fixture
def user_endpoint():
    return UserEndPoints

# User data for updating (parameterized for multiple sets of data)
@pytest.fixture
def update_user_data_fixture():
    return [
        {
            "name": "John Updated",
            "username": "johndoe_updated1",
            "email": "johndoe_updated1@example.com",
            "address": {
                "street": "123 Main St Updated",
                "suite": "Apt. 1 Updated",
                "city": "City A Updated",
                "zipcode": "12345",
                "geo": {"lat": "12.34", "lng": "56.78"}
            },
            "phone": "1-555-555-5551",
            "website": "johndoe_updated1.com",
            "company": {"name": "Company A", "catchPhrase": "Innovation at scale Updated", "bs": "tech"}
        },
        {
            "name": "Jane Updated",
            "username": "janesmith_updated2",
            "email": "janesmith_updated2@example.com",
            "address": {
                "street": "456 Elm St Updated",
                "suite": "Apt. 2 Updated",
                "city": "City B Updated",
                "zipcode": "67890",
                "geo": {"lat": "23.45", "lng": "67.89"}
            },
            "phone": "1-555-555-5552",
            "website": "janesmith_updated2.com",
            "company": {"name": "Company B", "catchPhrase": "Leading the future Updated", "bs": "business"}
        },
        {
            "name": "Alice Updated",
            "username": "alicejohnson_updated3",
            "email": "alicejohnson_updated3@example.com",
            "address": {
                "street": "789 Oak St Updated",
                "suite": "Apt. 3 Updated",
                "city": "City C Updated",
                "zipcode": "11223",
                "geo": {"lat": "34.56", "lng": "78.90"}
            },
            "phone": "1-555-555-5553",
            "website": "alicejohnson_updated3.com",
            "company": {"name": "Company C", "catchPhrase": "The future of tech Updated", "bs": "engineering"}
        }
    ]
