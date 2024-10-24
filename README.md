TaskNode (Still in Dev ...)

Efficient Task Management Platform | Built with Django & React

TaskNode is a modern task management system designed to help individuals and teams stay organized, track their tasks, and collaborate effectively. Combining the power of Django for the backend and React for the frontend, TaskNode ensures a smooth, responsive, and efficient experience for users.


🛠️ Tech Stack

    Frontend: React
    Backend: Django (Django REST Framework)
    Database: PostgreSQL (or any other you prefer / sqllite used in the dev phase)
    Authentication: JWT (JSON Web Tokens)
    Deployment: Docker / Nginx / Gunicorn (Optional)

🚀 Features

    🌟 User Management

        Sign up, log in, and secure authentication with JWT.
        Role-based access control (Admin, Manager, User).

    📋 Task Management

        Create, assign, and manage tasks.
        Set priorities, deadlines, and task categories.
        Track progress with task statuses: Pending, In Progress, Completed.

    👥 Collaboration Tools

        Assign tasks to team members.
        Task reviews and approvals by managers.

    📊 Analytics & Tracking

        Visualize task progress with detailed reports.
        Productivity insights for individual users and teams.

    🔒 Security Features

        Secure user data with Django’s authentication and JWT.
        Role-based access ensures fine-grained control over what users can do.

📚 Getting Started

1. Clone the repository

    |-----------------------------------------------------|
    | git clone https://github.com/MLaafoura/taskNode.git |
    | cd taskNode                                         |
    |-----------------------------------------------------|

2. Backend Setup (Django)

    Install dependencies:

    |--------------------------------------|
    |                                      |
    | pip install -r requirements.txt      |
    |                                      |
    | Run migrations and start the server: |
    |                                      |
    |                                      |
    |    python manage.py migrate          |
    |    python manage.py runserver        |
    |                                      |
    |--------------------------------------|

 3. Frontend Setup (React)

    Navigate to the frontend directory:

       |----------------------| 
       | cd tasknode-frontend |
       |----------------------|


    Install dependencies and start the development server:
    
    |--------------------|
    |    npm install     |
    |    npm start       |
    |--------------------|

4. Access the application

    Open your browser and navigate to http://localhost:3000 for the frontend and http://localhost:8000 for the backend API.


📂 Project Structure


taskNode/
├── taskNode/                   # Django backend folder
│   ├── manage.py               # Django management script          
│   └── ...
├── tasknode-frontend/           # React frontend folder
│   ├── public/
│   ├── src/
│   └── ...
├── .gitignore                   # Ignored files
├── README.md                    # Project documentation
└── ...


🛡️ Security and Best Practices

    JWT Authentication for secure API access.
    CSRF protection enabled for safe requests.
    Adheres to OWASP security guidelines.


🤝 Contributions

    We welcome contributions to TaskNode! Feel free to open an issue or submit a pull request for any improvements or bug fixes.


👨‍💻 Author

    Mouaad Laafoura

        https://github.com/MLaafoura
        https://www.linkedin.com/in/mouaad-laafoura-1aab1423b/


