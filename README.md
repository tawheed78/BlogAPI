# BlogAPI

This is a RESTful API for a blog, built using Django and Django Rest Framework.

## Installation

1. Clone this repository to your local machine using `git clone https://github.com/<your-username>/blogapi.git`.
2. Navigate to the cloned directory using `cd blogapi`.
3. Install the required packages by running `pip install -r requirements.txt`.
4. Create a `.env` file in the root directory and add your environment variables or remove the os command and put your own secret key and save while working on it locally.
5. Run the migrations using `python manage.py migrate`.
6. Start the development server using `python manage.py runserver`.

## Usage

1. To authenticate, send a `POST` request to `http://localhost:8000/login/` with your credentials (username and password) in the request body.
2. You will receive a JWT token in the response.
3. Use the token in the `Authorization` header of subsequent requests to the protected endpoints.
4. Use the available endpoints to create, read, update, and delete posts and comments, as well as like and search for posts.

## Endpoints

- `GET /` - retrieve all posts
- `GET /search/` - search for posts by keyword
- `POST /create/` - create a new post
- `GET /<int:pk>/` - retrieve a post by ID
- `PUT /<int:pk>/update/` - update a post by ID
- `DELETE /<int:pk>/delete/` - delete a post by ID
- `POST /<int:pk>/like/` - like a post by ID
- `POST /<int:pk>/comment/` - add a comment to a post by ID
- `GET /<username>/` - retrieve all posts by a user
- `POST /login/` - authenticate user and receive a JWT token
- `POST /token/refresh/` - refresh an expired JWT token

## Authentication

This API uses JSON Web Tokens (JWT) for authentication and authorization. To access protected endpoints, include a valid JWT token in the `Authorization` header of your request.

## Environment Variables

To run this project, you will need to set the following environment variables:

- `SECRET_KEY` - Django secret key
- `DEBUG` - set to `True` for development, `False` for production
- `ALLOWED_HOSTS` - comma-separated list of allowed hosts
- `JWT_ALGORITHM` - (default is `HS256`)
- `JWT_EXPIRATION_DELTA` - (default is `7 days`)





## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


