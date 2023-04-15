# Smart Project

Smart Project is a prototype web application aimed at teachers and students for sharing knowledge and publishing their work. The project implements a microservices architecture and uses gRPC communication between the services. The main features include user management, content management, and analytics.

## Features

- User management: registration, login, profile editing (using Google authentication for easy access)
- Content management: creating and managing content
- Analytics: gathering data from user behavior, deducing information, and visualizing the data in real-time (currently using Redis and Channels, planning to use Kafka and Plotly in the future)
- Technologies: Django, gRPC, Bootstrap CSS, PostgreSQL, Redis

## Microservices Architecture

The project is divided into two gRPC servers:

1. User Management and Content Management: These services are related and handle user registration, authentication, and content creation.
2. Analytics: This service is responsible for gathering data from user behavior, deducing information from the data, and visualizing the data in real-time.

## Installation

1. Clone the repository: `git clone https://github.com/YonatanLevyn/smart_proj.git`
2. Create and activate a virtual environment: `python -m venv venv_site` and `source venv_site/bin/activate`
3. Install the requirements: `pip install -r requirements.txt`
4. Configure the `settings.py` file with your local environment variables. See [Configuration](#configuration) for more details.
5. Run the Django application: `python manage.py runserver`

## Configuration

Before running the application, you'll need to configure the `settings.py` file with your local environment variables. You'll need to provide the following environment variables:

- `DJANGO_SECRET_KEY`: Django secret key
- `GOOGLE_CLIENT_ID`: Google OAuth client ID
- `GOOGLE_SECRET`: Google OAuth secret
- `GOOGLE_KEY`: Google OAuth key
- `DB_NAME`: PostgreSQL database name
- `DB_USER`: PostgreSQL database user
- `DB_PASSWORD`: PostgreSQL database password
- `DB_HOST`: PostgreSQL database host
- `DB_PORT`: PostgreSQL database port

You can set these environment variables in your shell or use a `.env` file.


## Contributing

Feel free to contribute to the project by opening issues, suggesting improvements, or submitting pull requests.

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).
