# EduConnect

EduConnect is a collaborative online learning platform designed for students, educators, and professionals to connect, communicate, and learn effectively. Users can join or create topic-based rooms, share knowledge, and communicate seamlessly through an integrated messaging system.

## Features
## 1. Room Management
Create, edit, and delete topic-based rooms.
Users can explore rooms based on their interests or create new ones.
Each room has a host with administrative privileges to manage participants and discussions.

## 2. User Authentication
Secure user registration and login functionality.
Authentication system with Django's built-in User model, extended for additional customization.
Role-based access control for managing room functionalities.

## 3. Real-Time Messaging
Participants can send messages within rooms for real-time discussions.
A structured and user-friendly messaging interface.
Messages are linked to both rooms and users for effective organization.

## 4. Activity Feed
Displays recent user activities and room interactions.
Enhances engagement by showcasing ongoing discussions and updates.

## 5. Mobile Responsiveness
Fully responsive design ensures accessibility across devices.
Optimized user experience for both desktop and mobile users.

## 6. Admin Panel
Administrative interface for managing users, rooms, topics, and messages.
Simplifies database interactions and ensures data integrity.


# Tech Stack
## Frontend
HTML5, CSS3, JavaScript: For building an interactive and responsive interface.
Bootstrap: To enhance the design and ensure responsiveness.
## Backend
Django: A robust Python framework for rapid development and secure functionality.
Django REST Framework: For creating RESTful APIs for room data and messaging.
## Database
SQLite: Lightweight database used for local development.
## Other Tools
Django Admin Panel: Simplified management of application data.
Postman: For API testing and debugging during development.

# Installation and Setup
## 1. Clone the Repository
git clone <repository_url>
cd EduConnect

## 2. Create and Activate Virtual Environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

## 3. Install Dependencies
pip install -r requirements.txt

## 4. Apply Database Migrations
python manage.py makemigrations
python manage.py migrate

## 5. Run the Development Server
python manage.py runserver

## 6. Access the Application
Visit http://127.0.0.1:8000 in your web browser.

# Usage

## For Users
Register or Login: Create an account or log in to an existing account.
Explore or Create Rooms: Join topic-based rooms or create your own.
Messaging: Engage in real-time discussions with participants.
Update Profile: Personalize your profile for better engagement.

## For Admins
Manage Rooms: Add, edit, or delete rooms.
Oversee Users: Monitor and manage user activities.
Handle Messages: Maintain a clean and efficient messaging system.

# API Endpoints
## Rooms
GET /api/rooms/: Retrieve a list of all rooms.
GET /api/rooms/:id: Retrieve a particular room based on their id.

## Messages
GET /api/messages/: Retrieve recent messages.

