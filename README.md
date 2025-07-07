# 📘 CaseBook - The Social Media Platform

**CaseBook** is a modern, scalable, and user-friendly social media platform inspired by Facebook. It allows users to connect, share, and interact through posts, likes, comments, and more. Built using **Flask** and **Node.js** for the backend, and a custom-designed frontend by Aliha, CaseBook aims to bring a unique social networking experience.

---

## 🌐 Live Demo

🚧 *Coming Soon* (Optional: Add deployed link here if available)

---

## 📦 Features

### 👤 User Features
- Register / Login (JWT Authentication)
- Profile page with avatar & bio
- Follow / Unfollow users
- View and manage friend lists
- Password encryption

### 📝 Posts & Feeds
- Create, edit, and delete posts
- Add images or links to posts
- Like / Unlike posts
- Comment on posts
- View global feed and personal timeline

### 💬 Comments & Interaction
- Real-time commenting system
- Reply to comments (nested replies)
- Like comments

### 📥 Notifications (coming soon)
- Get notified for likes, comments, and new followers

### 📁 Media Uploads
- Upload and share profile pictures, post media (images/videos)

### 🔒 Security
- Token-based authentication (JWT)
- CORS enabled
- Input validation

---

## 🛠 Tech Stack

| Category     | Technology                      |
|--------------|----------------------------------|
| **Frontend** | HTML5, CSS3, JavaScript          |
|              | Custom UI by Aliha              |
| **Backend**  | Flask (Python), Node.js (Express)|
| **Database** | PostgreSQL                      |
| **Auth**     | JWT (JSON Web Token)             |
| **ORM**      | SQLAlchemy (Flask)              |
| **API**      | RESTful APIs                     |

---

## 📁 Folder Structure


social-media-app/
├── app.py                      # Main Flask application
├── config.py                   # Configuration for database and JWT
├── manage.py                   # Utility script to reset the database
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation

├── /templates                  # All frontend HTML pages
│   ├── html.html
│   ├── Registeration.html
│   ├── login.html
│   ├── profile.html
│   ├── chat.html
│   ├── admin.html
│   ├── pages_groups.html
│   ├── search_results.html
│   └── other pages...

├── /static                     # Static files (CSS, JS, images)
│   ├── /css
│   │   └── html.css
│   ├── /js
│   │   └── html.js
│   └── /images
│       ├── avatars/
│       └── stories/

├── /models                     # Database models
│   ├── __init__.py
│   └── user.py

├── /routes                     # API route blueprints
│   ├── __init__.py
│   └── auth.py

├── /extensions                 # Reusable extensions (db, jwt)
│   └── __init__.py

---

## 🧠 How to Run

### 📌 Backend (Flask + Node.js)

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/casebook.git
   cd casebook/backend

