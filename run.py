from app import create_app
from db import db
import models.store, models.tag, models.item, models.user

app = create_app()

with app.app_context():
    db.create_all()

# Не викликаємо app.run() – Gunicorn зробить це сам
