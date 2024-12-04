# EduConnect

EduConnect is a collaborative online learning platform designed for students, educators, and professionals to connect, communicate, and learn effectively. Users can join or create topic-based rooms, share knowledge, and communicate seamlessly through an integrated messaging system.

## Features
### 1. Room Management
<p> Create, edit, and delete topic-based rooms. <br>
Users can explore rooms based on their interests or create new ones.<br>
Each room has a host with administrative privileges to manage participants and discussions. </p>

### 2. User Authentication
<p>Secure user registration and login functionality. <br>
Authentication system with Django's built-in User model, extended for additional customization. <br>
Role-based access control for managing room functionalities.</p>

### 3. Real-Time Messaging
<p>Participants can send messages within rooms for real-time discussions.<br>
A structured and user-friendly messaging interface.<br>
Messages are linked to both rooms and users for effective organization.</p>

### 4. Activity Feed
<p>Displays recent user activities and room interactions.<br>
Enhances engagement by showcasing ongoing discussions and updates.</p>

### 5. Mobile Responsiveness
<p>Fully responsive design ensures accessibility across devices.<br>
Optimized user experience for both desktop and mobile users.</p>

### 6. Admin Panel
<p>Administrative interface for managing users, rooms, topics, and messages.<br>
Simplifies database interactions and ensures data integrity.</p>


## Tech Stack
### Frontend
<p>HTML5, CSS3, JavaScript: For building an interactive and responsive interface.<br>
Bootstrap: To enhance the design and ensure responsiveness.</p>

### Backend
<p>Django: A robust Python framework for rapid development and secure functionality.<br>
Django REST Framework: For creating RESTful APIs for room data and messaging.</p>

### Database
<p>SQLite: Lightweight database used for local development.</p>

### Other Tools
<p>Django Admin Panel: Simplified management of application data.<br>
Postman: For API testing and debugging during development.</p>

## Installation and Setup

### 1. Clone the Repository
<p>git clone <repository_url> <br>
cd EduConnect </p>

### 2. Create and Activate Virtual Environment
<p>python -m venv env <br>
source env/bin/activate  # On Windows: env\Scripts\activate </p>

### 3. Install Dependencies
<p> pip install -r requirements.txt </p>

### 4. Apply Database Migrations
<p> python manage.py makemigrations <br>
python manage.py migrate </p>

### 5. Run the Development Server
<p> python manage.py runserver </p>

### 6. Access the Application
<p> Visit http://127.0.0.1:8000 in your web browser. </p>

## Usage

### For Users
<p> Register or Login: Create an account or log in to an existing account. <br>
Explore or Create Rooms: Join topic-based rooms or create your own. <br>
Messaging: Engage in real-time discussions with participants. <br>
Update Profile: Personalize your profile for better engagement.  </p>

### For Admins
<p> Manage Rooms: Add, edit, or delete rooms. <br>
Oversee Users: Monitor and manage user activities. <br>
Handle Messages: Maintain a clean and efficient messaging system. </p>

## API Endpoints
### Rooms
<p> GET /api/rooms/: Retrieve a list of all rooms. <br>
GET /api/rooms/:id: Retrieve a particular room based on their id. </p>

### Messages
<p> GET /api/messages/: Retrieve recent messages. </p>

