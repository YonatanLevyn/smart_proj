# Smart Project

Smart Project is a prototype web application aimed at teachers and students for sharing knowledge and publishing their work. The project implements a microservices architecture and uses gRPC communication between the services.

## Microservices Architecture

The project is designed using a microservices architecture and consists of four distinct services:

1. User Management: Handles user registration, authentication, and profile editing, leveraging Google authentication for easy access.
2. Content Management: Facilitates creating and managing various types of content, ensuring seamless organization and distribution.
3. Courses: A dedicated service for managing courses, enabling course creation, lesson management, and related functionalities.
4. Analytics: Gathers data from user behavior, analyzes the information, and visualizes the data in real-time, providing insights into user engagement and preferences.

Each service is responsible for different aspects of the application, promoting maintainability and scalability as the project grows.

## Technologies

- Django
- gRPC
- Bootstrap CSS
- PostgreSQL
- Redis
- Channels

## Installation

1. Clone the repository: `git clone https://github.com/YonatanLevyn/smart_proj.git`
2. Create and activate a virtual environment: `python -m venv venv_site` and `source venv_site/bin/activate`
3. Install the requirements: `pip install -r requirements.txt`
4. Configure the `settings.py` file with your local environment variables. For demo mode, you only need to provide the `DJANGO_SECRET_KEY`. See [Configuration](#configuration) for more details.
5. Run the Django application using Daphne: `daphne site_proj.asgi:application`

## Configuration

Before running the application, you'll need to configure the application with your local environment variables. 
For demo mode, you'll need to provide just one environment variable:

- `DJANGO_SECRET_KEY`: Django secret key

You can set this environment variable in your `.env.example` file and renaming it to `.env`.

For full mode, you'll need to provide additional environment variables related to Google authentication and PostgreSQL configuration. You can find these in the `.env.example` file. Remember to set the `DEMO_MODE` line in the `.env` file to `False` when using the full mode.

Once the environment variables are set, you can proceed to run the application.


## Contributing

Feel free to contribute to the project by opening issues, suggesting improvements, or submitting pull requests.

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

