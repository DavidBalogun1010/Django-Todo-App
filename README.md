
# Django ToDo App

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![Django](https://img.shields.io/badge/Django-5.x-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

A simple, full-featured ToDo application built with **Django**.  
It allows users to **create, update, delete, and track tasks**, assign due dates, and mark tasks as resolved. The app features a responsive **Bootstrap 5** frontend with clean UI and CSS styling.

---

## 📝 Project Overview

This Django ToDo app demonstrates a real-world CRUD web application.  
It covers:

- Django models and database relationships
- Forms and form validation
- Class-based and function-based views
- Templating with reusable base template
- Static files integration (CSS and Bootstrap)
- Automated tests

---

## ⚡ Features

- Create new tasks with title, description, and due date
- Edit existing tasks
- Delete tasks with confirmation
- Mark tasks as resolved or pending
- List tasks with clear status indicators (Pending / Completed)
- Fully responsive UI using Bootstrap 5
- Custom CSS styling for improved UX
- Unit tests covering all core functionality

---

## 🛠 Tech Stack

- **Backend:** Django 5.x, Python 3.11+  
- **Frontend:** HTML5, CSS3, Bootstrap 5  
- **Database:** SQLite (default)  
- **Testing:** Django `TestCase`  

---

todo_project/
│
├── todo_project/ # Django project configuration
│ ├── settings.py
│ └── urls.py
│
├── tasks/ # Django app
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ ├── urls.py
│ └── templates/tasks/
│ ├── task_list.html
│ ├── task_form.html
│ └── task_confirm_delete.html
│ └── static/tasks/style.css
│
├── templates/ # Global templates
│ └── base.html
│
└── manage.py


---

## 🚀 Installation & Setup

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/django-todo-app.git
cd django-todo-app


Create and activate a virtual environment:

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Apply migrations:

python manage.py migrate


Run the development server:

python manage.py runserver


Open the app in your browser:

http://127.0.0.1:8000

🎯 Usage

Navigate to the homepage to see the list of tasks.

Click + Add Task to create a new task.

Use action buttons to Edit, Delete, or Toggle Resolved status.

Tasks display Pending or Completed badges.

Due dates are displayed for each task.

Optional: You can style further or add Bootstrap components for a modern dashboard look.

🧪 Running Tests

Run all automated tests:

python manage.py test


Tests cover:

Task creation

Task editing

Task deletion

Marking task as resolved

Task listing

📷 Screenshots

(Add screenshots of your app here)

Example:

Task List Page


Add/Edit Task Form


🌟 Future Enhancements

Add user authentication (multi-user support)

Add task priority levels and filters

Add REST API with Django REST Framework

Improve UI with drag-and-drop task ordering

Notifications for overdue tasks

📜 License

This project is licensed under the MIT License.
© 2025 Your Name

🙋‍♂️ Author

Your Name – GitHub

## 📁 Project Structure

