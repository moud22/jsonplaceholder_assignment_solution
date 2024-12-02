### JSON Placeholder Assignment solution
A comprehensive automation testing framework designed for the JSONPlaceholder API, showcasing advanced techniques with pytest for Users, Posts, and Comments modules. This framework integrates modular test structures, dynamic data handling, and interactive reporting tools like Allure and pytest-html, making it a robust solution for scalable API testing.

### Clone Project
1. Clone the repository
```git clone https://github.com/moud22/jsonplaceholder_assignment_solution.git```

2. Change directory
```cd assignment_solution```

### Steps to run the test script

1. Create Virtual Environment
```python3 -m venv cenv```

2. Activate Virtual Environment
```source cenv/bin/activate```

3. Install dependencies
```pip3 install -r requirements.txt```

4. Run the script using PyTest
```python3 -m pytest -s```

### Steps to generate and see the test script reports using allure

1. Finish the steps of running the project
```python3 -m pytest -s```

2. Run Allure generate command
```allure generate reports/allure-results -o reports/allure-report --clean```

3. Run the below allure command to view the report
```allure open reports/allure-report```

4. After the above comment has run, allure will create a server for displaying the report, copy the link and open it in any of your browser
```example link : http://127.0.1.1:43571/```\
Important note : ```the generated http link will be active until it's active, so in order to close the report, please enter ctrl+c in terminal```

### Project Structure:
- `common_utils/`: Contains all the API call methods required to run our modules, Posts, Users and Comments.
- `config/`: Contains the base_url of our website(As of Now). We can keep this file for future use so that we can add all the header detils, authentication details, cookies etc.
- `requirements.txt`: Lists the dependencies for the project.
- `comments/`: contains all the endpoints of comment module, test cases and their respective fixture files.
- `posts/`: contains all the endpoints of post module, test cases and their respective fixture files.
- `users/`: contains all the endpoints of users module, test cases and their respective fixture files.
- `fixtures/`: contains API endpoints operations (create, retrieve), multiple sets of data for testing(Data driven test approach).
- `reports/`: contains all the report files which gets generated after running the automation script.
- `pytest.ini`: contains configurations of pytest, as of now, only allure reporting configurations has been added. This is a configuration file used by pytest to set global settings and behaviors for your test suite. It allows you to define options, plugins, markers, and other configurations in a central location, making your test suite easier to manage and customize.
- `script_logger.log`: contains log details.
