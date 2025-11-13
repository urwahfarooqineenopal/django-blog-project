Django Blog Project

A simple yet functional **Blog Web Application** built with Django. This project allows users to create, read, update, and delete blog posts through a user-friendly interface.  
It includes styled pages, dynamic views, and Django’s ORM for database operations.

Features

-Create, Edit, and Delete blog posts  
- List all blog posts  
- View individual blog details  
- Uses Django ORM with SQLite  
- Styled with Bootstrap for a clean UI  
- Admin panel to manage posts  

Project Setup Instructions

python manage.py runserver
Visit the app at  http://127.0.0.1:8000/
and the admin panel at  http://127.0.0.1:8000/admin/

Project Structure



blog_project/
│
├── blog/                  # Main app folder
│   ├── migrations/        # Database migrations
│   ├── templates/blog/    # HTML templates
│   ├── static/            # CSS, JS, Images
│   ├── models.py          # Blog model
│   ├── views.py           # Logic for each page
│   ├── urls.py            # URL routes for the blog app
│   └── forms.py           # Blog form for CRUD operations
│
├── blog_project/          # Project configuration folder
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py / asgi.py  # Deployment files
│
├── manage.py              # Django management script
└── README.md              # Project documentation


Screenshots

Admin Panel (Single Blog Entry Edited)
Description:
This screenshot shows the Django Admin Panel where the blog “Capstone Blog” has been successfully edited. The success message (“The blog ‘Capstone Blog’ was changed successfully.”) confirms that the CRUD operations for the Blog model are working as expected.
refer to Screenshots
 

Admin Panel (Multiple Blogs Listed)
Description:
This view displays the list of all blogs created in the Django admin. It shows two blog entries: “Capstone Blog” and “Capstone Blog2”. This verifies that multiple records can be created, stored, and retrieved through the Django ORM.
 refer to Screenshots

Frontend Blog Homepage
File: css.JPG
Description:
This is the frontend of the blog website. The home page displays a welcoming banner — “Welcome to My Blog” — and lists all published blog posts such as Capstone Blog, Capstone Blog2, and Testing forms. The design includes custom CSS styling to enhance presentation, fulfilling the styling requirement of the project.
refer to Screenshots

ORM ScreenShot
Description:
This screenshot displays the Django ORM in action using the interactive shell.
The terminal shows queries such as:
•	Blog.objects.all() → fetching all blog entries
•	Blog.objects.get(id=1) → retrieving a specific blog post by ID
•	Blog.objects.filter(title__icontains=Blog) → filtering posts containing a keyword in the title

refer to Screenshots

Add Blog Page (Create New Post)
Description:
This screenshot shows the Add Blog page where users can create a new blog entry using a simple form.
The form includes:
•	Title Field: Allows the user to enter the blog title (e.g., “Capstone Blog 3”).
•	Content Field: A text area for entering the main content or body of the post.
•	Save Button: On clicking Save, the form submits the data and saves it to the database using Django’s BlogForm and ORM logic.
After submission, the user is automatically redirected to the blog list view (/blogs/), where the new post appears along with previously created ones.
This functionality demonstrates Django’s ModelForm usage, form validation, and redirection after successful save — satisfying the Create (C) operation in the CRUD workflow.
 
refer to Screenshots

Tech Stack
Backend: Django 5.x
Frontend: HTML, CSS, Bootstrap
Database: SQLite
Language: Python 3.12

Author
Urwah Farooqi


