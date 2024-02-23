# RESTful API Project with Authentication and CSRF Protection

This Django project is a RESTful API that requires authentication and protection against Cross-Site Request Forgery (CSRF) attacks. Users must follow an authentication process to obtain an authentication token, then use that token to obtain a CSRF token, and finally use both tokens to access a "Hello world" function.

## Installation

1. Install Django and Django REST Framework:

    ```
    pip install django djangorestframework
    ```

2. Clone the Repository:

    ```
    git clone <repository_url>
    ```

3. Create Virtual Environment (Optional but Recommended):

    ```
    python -m venv myenv
    ```

4. Activate Virtual Environment (Optional):

    **Windows:**

    ```
    myenv\Scripts\activate
    ```

    **Linux/macOS:**

    ```
    source myenv/bin/activate
    ```
    
5. Configure Database:

    Set up your database configuration in `settings.py`.

6. Run Migrations:

    ```
    python manage.py migrate
    ```

## Deployment

1. Start Development Server:

    ```
    python manage.py runserver
    ```

    The API will be accessible at `http://localhost:8000/`.

## Routes

The following routes are provided by the API:

- `/test/`: Endpoint to obtain the CSRF token. Requires authentication.
- `/login/`: Endpoint for user authentication. Requires username and password in the request body.
- `/helloworld/`: Endpoint to access the "Hello world" function. Requires authentication and CSRF token in the request headers.

## Authentication

To access the API endpoints, users must authenticate by following these steps:

1. Send a POST request to `/login/` with the username and password in the request body.
2. Obtain the authentication token from the response.
3. Include the authentication token in the headers of all subsequent requests.

## Accessing the "Hello world" Function

After obtaining both the authentication and CSRF tokens, users can access the "Hello world" function by following these steps:

1. Send a GET or POST request to `/helloworld/`.
2. Include both the authentication and CSRF tokens in the headers of the request.
