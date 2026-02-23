🚀 Full Stack Docker App

Flask + PostgreSQL + Docker + AWS EC2

📌 Project Overview

This project demonstrates how to build and deploy a full-stack application using:

Flask (Python backend)

PostgreSQL (Database)

Docker (Containerization)

Docker Compose (Multi-container setup)

AWS EC2 (Ubuntu) for deployment

The application connects a Flask server to a PostgreSQL database running inside Docker containers.

🗂 Project Structure
full-stack-docker-app/
│
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── docker-compose.yml
└── README.md
⚙️ How the Application Works

The Flask container runs the backend server.

The PostgreSQL container runs the database.

Docker Compose creates a private network so both containers can communicate.

The app connects to the database using the service name db as the host.

The Flask app is exposed on port 5000 (or port 80 if configured).

🐳 Running the Project
1️⃣ Clone the Repository
git clone https://github.com/YOUR_USERNAME/full-stack-docker-app.git
cd full-stack-docker-app
2️⃣ Build and Start Containers
docker-compose up --build -d

This command:

Builds the Docker image

Starts PostgreSQL

Starts the Flask app

Runs everything in the background

3️⃣ Verify Containers Are Running
docker ps

You should see:

flask-app

postgres-db

4️⃣ Access the Application
If running locally:
http://localhost:5000
If running on AWS EC2:
http://YOUR_PUBLIC_IP:5000

Make sure port 5000 (or 80) is open in your AWS Security Group.

🛑 Stop the Application
docker-compose down
🗄 Database Configuration

Inside docker-compose.yml, the database is configured with:

User: postgres

Password: postgres

Database: postgres

Host: db

Port: 5432

Flask connects using these credentials.

🧪 Debugging
View logs
docker-compose logs
View logs for Flask only
docker-compose logs web
Restart containers
docker-compose down
docker-compose up --build -d
📚 What This Project Demonstrates

Containerizing a Python Flask app

Connecting services using Docker networking

Running multi-container apps with Docker Compose

Deploying Docker applications to AWS EC2

Debugging container errors

Exposing container ports to the internet

🔮 Future Improvements

Add Nginx reverse proxy

Add HTTPS (SSL certificate)

Use environment variables with .env

Add CI/CD pipeline

Add frontend (React / Vue)

Deploy using ECS or Kubernetes
