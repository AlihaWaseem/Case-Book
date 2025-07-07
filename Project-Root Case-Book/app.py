from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from datetime import datetime
from routes.auth import auth_bp
from extensions import db, jwt
from sqlalchemy import text

app = Flask(__name__)
CORS(app)
app.config.from_object("config.Config")

db.init_app(app)
jwt.init_app(app)
from flask import render_template

app.register_blueprint(auth_bp, url_prefix="/api/auth")

@app.route("/register.html")
def register_page():
    return render_template("register.html")

@app.route("/login.html")
def login_page():
    return render_template("login.html")

@app.route('/')
def home():
    return render_template('html.html')

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
    content = db.Column(db.Text)
    media_url = db.Column(db.String(255))
    media_type = db.Column(db.String(10))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Like(db.Model):
    __tablename__ = 'likes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

@app.route("/test-db")
def test_db():
    try:
        result = db.session.execute(
            text("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
        )
        tables = [row[0] for row in result]
        return jsonify({"connected": True, "tables": tables})
    except Exception as e:
        return jsonify({"connected": False, "error": str(e)})

@app.route("/api/posts", methods=["POST"])
def create_post():
    data = request.json
    post = Post(
        user_id=data['user_id'],
        content=data.get('content'),
        media_url=data.get('media_url'),
        media_type=data.get('media_type')
    )
    db.session.add(post)
    db.session.commit()
    return jsonify({"message": "Post created", "post_id": post.id}), 201

@app.route("/api/posts", methods=["GET"])
def get_posts():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    result = []
    for post in posts:
        result.append({
            "id": post.id,
            "user_id": post.user_id,
            "content": post.content,
            "media_url": post.media_url,
            "media_type": post.media_type,
            "created_at": post.created_at.isoformat()
        })
    return jsonify(result)

@app.route("/api/comments", methods=["POST"])
def add_comment():
    data = request.json
    comment = Comment(
        user_id=data['user_id'],
        post_id=data['post_id'],
        text=data['text']
    )
    db.session.add(comment)
    db.session.commit()
    return jsonify({"message": "Comment added"}), 201

@app.route("/api/likes", methods=["POST"])
def like_post():
    data = request.json
    existing = Like.query.filter_by(user_id=data['user_id'], post_id=data['post_id']).first()
    if existing:
        db.session.delete(existing)
        db.session.commit()
        return jsonify({"message": "Unliked"})
    like = Like(user_id=data['user_id'], post_id=data['post_id'])
    db.session.add(like)
    db.session.commit()
    return jsonify({"message": "Liked"}), 201

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
