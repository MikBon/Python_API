from app import create_app
from db import db
import models  # Імпорт потрібен для реєстрації моделей

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
