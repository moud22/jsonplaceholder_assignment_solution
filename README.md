### Clone Project



### Steps to run the test script

1. Create Virtual Environment
```python3 -m venv cenv```

2. Activate Virtual Environment
```source cenv/bin/activate```

3. Install dependencies
```pip3 install -r requirements.txt```

4. Run the script using PyTest
```python3 -m pytest -s```

### Project Structure:
- `common_utils/`: Contains all the API call methods required to run our modules, Posts, Users and Comments
- `config/`: Contains the base_url of our website(As of Now). We can keep this file for future use so that we can add all the header detils, authentication details, cookies etc.
- `requirements.txt`: Lists the dependencies for the project.
- `comments`/: contains all the 
