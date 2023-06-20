# Smart Project

Smart Project is a prototype web platform aimed at teachers and students for sharing knowledge and publishing their work. 

# Project Structure

This Django project is organized into different applications, with each one exposing its own REST APIs:

courses: Handles all operations related to courses and their lessons.
users: Handles user registration, login, and profile management.
... (more services will be added, like profile and analyze services)
In the future, we plan to separate these services each with their related database. A reverse proxy will sit between the client-side and the server-side. The services will likely communicate through a message queue.
