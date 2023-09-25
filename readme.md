Blog Application
The Blog Application is a versatile platform that allows users to create, manage, and share their blogs. It provides seamless user authentication using Django's built-in HTTP authentication system and ensures data isolation between users. Key features include:

Features
User Authentication:

User registration with unique usernames and secure password storage.
User login using Django's HTTP authentication system.
Blog CRUD Operations:

Create: Users can create new blog posts.
Read: View your own blog posts and posts from other users.
Update: Modify and update your existing blog posts.
Delete: Delete your own blog posts.
Data Isolation:

Strict data isolation ensures that users can only access, edit, and delete their own blog posts.

Getting Started:
1.Run Django migrations to create the database schema using python manage.py migrate.

2.Create a superuser account for admin access using python manage.py createsuperuser.

3.Start the Django development server using python manage.py runserver.

4.Access the application in your web browser at http://localhost:8000.

Usage
To create a new blog post, log in with your credentials and navigate to the "New Post" page.
To read and interact with other users' blog posts, explore the Home section.
