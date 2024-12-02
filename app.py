from flask import Flask
from pymongo import MongoClient
from config import Config
from routes.threads_routes import create_thread_routes
from routes.users_routes import create_user_routes

app = Flask(__name__)
app.config.from_object(Config)

# MongoDB Connection
client = MongoClient(app.config["MONGO_URI"])
db = client["threads_db"]

# Register Blueprints
app.register_blueprint(create_thread_routes(db))
app.register_blueprint(create_user_routes(db))

if __name__ == "__main__":
    app.run(debug=True)
