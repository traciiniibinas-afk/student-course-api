from flask import Flask, jsonify, render_template_string
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# ==========================================
# SAMPLE COURSE DATA
# ==========================================

courses = [
    {
        "id": 1,
        "code": "CS 101",
        "name": "Introduction to Computing",
        "description": "Learn the fundamentals of computers."
    },
    {
        "id": 2,
        "code": "IT 102",
        "name": "Web Development",
        "description": "Learn how to build websites."
    },
    {
        "id": 3,
        "code": "CS 103",
        "name": "Database Management",
        "description": "Learn how databases store information."
    },
    {
        "id": 4,
        "code": "IT 104",
        "name": "Networking Fundamentals",
        "description": "Learn the basics of computer networks."
    },
    {
        "id": 5,
        "code": "CS 105",
        "name": "Programming Fundamentals",
        "description": "Learn basic programming concepts."
    },
    {
        "id": 6,
        "code": "IT 106",
        "name": "Systems Integration",
        "description": "Learn how different systems communicate."
    }
]


# ==========================================
# HOMEPAGE / API DASHBOARD
# ==========================================

@app.route("/", methods=["GET"])
def home():

    html = """
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Student Course API Dashboard</title>

        <style>

            * {
                box-sizing: border-box;
            }

            body {
                font-family: Arial, sans-serif;
                background: #f1f5f9;
                margin: 0;
                padding: 0;
                color: #1e293b;
            }

            header {
                background: #172554;
                color: white;
                padding: 25px 40px;
            }

            header h1 {
                margin: 0;
                font-size: 28px;
            }

            header p {
                margin-bottom: 0;
                color: #cbd5e1;
            }

            .container {
                max-width: 1100px;
                margin: 30px auto;
                padding: 0 20px;
            }

            .welcome {
                margin-bottom: 25px;
            }

            .welcome h2 {
                margin-bottom: 8px;
            }

            .stats {
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 20px;
                margin-bottom: 25px;
            }

            .stat-card {
                background: white;
                padding: 25px;
                border-radius: 12px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            }

            .stat-card h3 {
                margin: 0 0 10px;
                color: #64748b;
                font-size: 14px;
            }

            .stat-card .number {
                font-size: 30px;
                font-weight: bold;
                color: #1d4ed8;
            }

            .status {
                color: #16a34a;
                font-weight: bold;
            }

            .section {
                background: white;
                padding: 25px;
                border-radius: 12px;
                margin-bottom: 25px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            }

            .section h2 {
                margin-top: 0;
                color: #172554;
            }

            .table-wrapper {
                overflow-x: auto;
            }

            table {
                width: 100%;
                border-collapse: collapse;
                min-width: 600px;
            }

            th {
                background: #1e3a8a;
                color: white;
                padding: 14px;
                text-align: left;
            }

            td {
                padding: 14px;
                border-bottom: 1px solid #e2e8f0;
            }

            tr:hover td {
                background: #f8fafc;
            }

            .endpoint {
                display: flex;
                justify-content: space-between;
                align-items: center;
                gap: 12px;
                padding: 13px;
                margin-bottom: 10px;
                background: #f8fafc;
                border-radius: 8px;
                flex-wrap: wrap;
            }

            .method {
                background: #dcfce7;
                color: #166534;
                padding: 5px 9px;
                border-radius: 5px;
                font-size: 12px;
                font-weight: bold;
            }

            a {
                color: #2563eb;
                text-decoration: none;
            }

            a:hover {
                text-decoration: underline;
            }

            .endpoint a {
                font-weight: bold;
            }

            footer {
                text-align: center;
                padding: 25px;
                color: #64748b;
                font-size: 13px;
            }

            @media (max-width: 600px) {
                header {
                    padding: 22px;
                }

                header h1 {
                    font-size: 22px;
                }

                .container {
                    margin-top: 20px;
                }

                .stats {
                    grid-template-columns: 1fr;
                }

                .section {
                    padding: 18px;
                }

                .endpoint {
                    align-items: flex-start;
                }
            }

        </style>
    </head>

    <body>

        <header>
            <h1>Student Course API</h1>
            <p>System Integration and Architecture</p>
        </header>

        <main class="container">

            <div class="welcome">
                <h2>API Dashboard</h2>
                <p>
                    Welcome to the Student Course API.
                    This dashboard provides an overview of the
                    available courses and API endpoints.
                </p>
            </div>

            <!-- SYSTEM STATISTICS -->

            <div class="stats">

                <div class="stat-card">
                    <h3>API STATUS</h3>
                    <div class="status">
                        ● Running
                    </div>
                    <p>Student Course API is operational.</p>
                </div>

                <div class="stat-card">
                    <h3>TOTAL COURSES</h3>
                    <div class="number">
                        {{ total }}
                    </div>
                    <p>Available sample courses</p>
                </div>

            </div>


            <!-- COURSE TABLE -->

            <div class="section">

                <h2>Available Courses</h2>

                <div class="table-wrapper">

                    <table>

                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Course Code</th>
                                <th>Course Name</th>
                                <th>Description</th>
                            </tr>
                        </thead>

                        <tbody>

                            {% for course in courses %}

                            <tr>
                                <td>{{ course.id }}</td>
                                <td>{{ course.code }}</td>
                                <td>{{ course.name }}</td>
                                <td>{{ course.description }}</td>
                            </tr>

                            {% endfor %}

                        </tbody>

                    </table>

                </div>

            </div>


            <!-- API ENDPOINTS -->

            <div class="section">

                <h2>Available API Endpoints</h2>

                <p>
                    Click an endpoint to view its JSON response.
                </p>

                <div class="endpoint">
                    <span>
                        <span class="method">GET</span>
                        /api/health
                    </span>
                    <a href="/api/health">Test Endpoint →</a>
                </div>

                <div class="endpoint">
                    <span>
                        <span class="method">GET</span>
                        /api/courses
                    </span>
                    <a href="/api/courses">View Courses →</a>
                </div>

                <div class="endpoint">
                    <span>
                        <span class="method">GET</span>
                        /api/courses/1
                    </span>
                    <a href="/api/courses/1">View Course 1 →</a>
                </div>

                <div class="endpoint">
                    <span>
                        <span class="method">GET</span>
                        /api/courses/9999
                    </span>
                    <a href="/api/courses/9999">Test Invalid Course →</a>
                </div>

            </div>

        </main>

        <footer>
            Student Course API | Backend Development
            <br>
            System Integration and Architecture
        </footer>

    </body>

    </html>
    """

    return render_template_string(
        html,
        courses=courses,
        total=len(courses)
    )


# ==========================================
# API ENDPOINT 1: HEALTH CHECK
# ==========================================

@app.route("/api/health", methods=["GET"])
def health():

    return jsonify({
        "status": "ok",
        "message": "Student Course API is running",
        "courses": len(courses)
    })


# ==========================================
# API ENDPOINT 2: GET ALL COURSES
# ==========================================

@app.route("/api/courses", methods=["GET"])
def get_courses():

    return jsonify(courses)


# ==========================================
# API ENDPOINT 3: GET SINGLE COURSE
# ==========================================

@app.route("/api/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):

    course = next(
        (c for c in courses if c["id"] == course_id),
        None
    )

    if course is None:

        return jsonify({
            "error": "Course not found",
            "status": 404
        }), 404

    return jsonify(course)


# ==========================================
# APPLICATION STARTUP
# ==========================================

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
    )
