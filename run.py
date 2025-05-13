from app import create_app
from db import db
from models import user, item, store, tag  

app = create_app()

with app.app_context():
    db.create_all()
