# routes/auth.py
from flask import Blueprint, request, jsonify
from extensions import db  
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from models.user import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    try:
        data = request.json or {}
        print("📥 Register incoming:", data)

        name = data.get("name")
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if not all([name, username, email, password]):
            return jsonify({"error": "All fields are required"}), 400

        if User.query.filter_by(email=email).first():
            return jsonify({"error": "Email already registered"}), 400
        if User.query.filter_by(username=username).first():
            return jsonify({"error": "Username already taken"}), 400

        new_user = User(
            fullname=name,  
            username=username,
            email=email,
            password_hash=generate_password_hash(password)
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully", "user_id": new_user.id}), 201
    except Exception as e:
        print("🔥 SERVER ERROR:", str(e))
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500



# ✅ LOGIN ROUTE
@auth_bp.route("/login", methods=["POST"])
def login():
    try:
        data = request.json
        print("📥 Login data:", data)

        user = User.query.filter_by(email=data["email"]).first()

        if not user or not check_password_hash(user.password_hash, data["password"]):
            return jsonify({"error": "Invalid credentials"}), 401

        token = create_access_token(identity=user.id)
        
        return jsonify({
            "message": "Login successful",
            "token": token,
            "user_id": user.id,
            "username": user.username,
            "avatar_url": user.avatar_url  # ✅ send this to frontend
        }), 200

    except Exception as e:
        print("🔥 SERVER ERROR:", str(e))
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500

    
