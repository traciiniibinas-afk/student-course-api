# Student Course API – Python Flask

## Project Description

The Student Course API is a backend application developed for Laboratory Activity 3. It provides course information through REST API endpoints using JSON responses.

The API contains six fictional courses and allows applications to retrieve course information.

## Technologies Used

- Python
- Flask
- Flask-CORS
- Gunicorn
- GitHub
- Render

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/health` | Checks if the API is running. |
| GET | `/api/courses` | Retrieves all six courses. |
| GET | `/api/courses/1` | Retrieves a specific course. |
| GET | `/api/courses/9999` | Demonstrates a 404 response. |

## Installation and Setup

1. Install Python.
2. Clone this repository.
3. Open the project folder in a terminal.
4. Install the dependencies:

```bash
pip install -r requirements.txt
```

5. Run the application locally:

```bash
python app.py
```

The API will run locally on port 5000 by default.

## Deployment

The Python Flask API is deployed using Render as a Web Service.

**Python Flask API URL:**

https://student-course-api-python.onrender.com

**API Testing Links:**

- Health Check: https://student-course-api-python.onrender.com/api/health
- All Courses: https://student-course-api-python.onrender.com/api/courses
- Specific Course: https://student-course-api-python.onrender.com/api/courses/1
- Invalid Course: https://student-course-api-python.onrender.com/api/courses/9999

The application uses Gunicorn as its production server and is connected to GitHub for automatic deployment.

## Project Limitations

This project uses fictional sample course data stored directly in the Python application. It does not use a database or user authentication.

It is a basic backend API prototype created for educational purposes.
