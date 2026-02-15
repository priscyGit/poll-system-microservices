# Poll System Microservices Project

## Description
This project is a microservices-based polling system built using **FastAPI**, **Docker**, and **MySQL**.

The system consists of two independent services:

- **User Service** – manages users and registration
- **Poll Service** – manages polls, answers, and statistics

Each service runs in its own Docker container and uses a separate MySQL database.

---

## Architecture

- Architecture: Microservices (User Service + Poll Service)
- Communication: REST API
- Framework: FastAPI
- Database: MySQL (separate database per service)
- ORM: SQLAlchemy
- Containerization: Docker & Docker Compose

Services communicate through the internal Docker network.

---

## Project Structure

---

## How to Run the Project

1. Clone the repository

2. Open a terminal inside the project folder

3. Run the following command:

```bash
docker compose up --build