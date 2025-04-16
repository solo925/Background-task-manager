# Django Background Task Manager

A robust task scheduling and background processing system built with Django, Celery, Redis, and Flower.

## Features

- **Task Management**: Create, monitor, and track various types of background tasks
- **Asynchronous Processing**: Handle time-consuming operations without blocking your web requests
- **Real-time Monitoring**: Track task progress and status with Flower dashboard
- **RESTful API**: Programmatically create and monitor tasks
- **Clean UI**: Bootstrap-based interface for easy task management
- **Docker Support**: Easy deployment with Docker and Docker Compose

## Technology Stack

- **Django**: Web framework
- **Celery**: Distributed task queue
- **Redis**: Message broker and result backend
- **Flower**: Celery monitoring tool
- **Bootstrap**: Frontend styling
- **Docker**: Containerization

## Screenshots

![Task List](/screenshots/task-list.png)
![Task Detail](/screenshots/task-detail.png)
![Flower Dashboard](/screenshots/flower-dashboard.png)

## Installation

### Prerequisites

- Python 3.8 or higher
- Redis
- Docker (optional)

### Option 1: Local Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/django-task-manager.git
cd django-task-manager
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Copy .env.example to .env and update settings
```bash
cp .env.example .env
```

5. Run database migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser
```bash
python manage.py createsuperuser
```

7. Run Redis (install if needed)
```bash
redis-server
```

8. Start the Django server
```bash
python manage.py runserver
```

9. In a new terminal, start the Celery worker
```bash
celery -A task_manager worker --loglevel=info
```

10. In another terminal, start Flower
```bash
celery -A task_manager flower
```

### Option 2: Docker Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/django-task-manager.git
cd django-task-manager
```

2. Copy .env.example to .env and update settings
```bash
cp .env.example .env
```

3. Build and start the containers
```bash
docker-compose up -d
```

4. Create a superuser
```bash
docker-compose exec web python manage.py createsuperuser
```

## Usage

1. Access the web interface at http://localhost:8000/
2. Log in with the superuser credentials
3. Create new tasks through the interface
4. Monitor task progress on the task detail page
5. View Flower dashboard at http://localhost:5555/ for detailed monitoring

## API Usage

### Create a task
```bash
curl -X POST http://localhost:8000/tasks/api/tasks/create/ \
  -H "Content-Type: application/json" \
  -d '{"name":"API Test Task","description":"Task created via API","task_type":"data_processing"}'
```

### Get task status
```bash
curl -X GET http://localhost:8000/tasks/api/tasks/1/
```

### List tasks
```bash
curl -X GET http://localhost:8000/tasks/api/tasks/
```

## Task Types

The system currently supports the following task types:

- **Data Processing**: Simulates processing of data
- **Email Campaign**: Simulates sending bulk emails
- **Report Generation**: Simulates generating complex reports
- **Other**: Generic task type for custom processing

## Project Structure

```
task_manager/
├── manage.py
├── task_manager/            # Django project settings
│   ├── __init__.py
│   ├── celery.py            # Celery configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tasks/                   # Django app for task management
│   ├── __init__.py
│   ├── admin.py             # Admin interface configuration
│   ├── api.py               # API endpoints
│   ├── apps.py
│   ├── forms.py             # Task creation forms
│   ├── models.py            # Task data model
│   ├── tasks.py             # Celery task definitions
│   ├── templates/           # HTML templates
│   ├── urls.py              # URL routing
│   └── views.py             # View controllers
├── Dockerfile               # Docker configuration
├── docker-compose.yml       # Docker Compose configuration
└── requirements.txt         # Python dependencies
```

## Development

### Adding a New Task Type

1. Define the task processing function in `tasks/tasks.py`
2. Add the task type to the choices in `tasks/forms.py`
3. Add any specific handling in the `process_task` function

### Custom Task Processing

You can customize the task processing logic by modifying the functions in `tasks/tasks.py`.

## Production Deployment

For production deployment:

1. Set appropriate environment variables (see .env.example)
2. Use proper PostgreSQL database instead of SQLite
3. Configure proper security settings for Redis
4. Set up HTTPS
5. Consider using Gunicorn/uWSGI for serving Django
6. Configure supervisor or systemd to manage Celery workers
7. Set up authentication for Flower dashboard

## License

MIT License

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request