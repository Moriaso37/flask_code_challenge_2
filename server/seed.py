from app import app, db
from models.guest import Guest
from models.episode import Episode
from datetime import date

with app.app_context():
    db.drop_all()
    db.create_all()

    g1 = Guest(name="Tom Hanks", occupation="Actor")
    g2 = Guest(name="Taylor Swift", occupation="Singer")
    e1 = Episode(date=date(2025, 6, 24), number=1)
    e2 = Episode(date=date(2025, 6, 25), number=2)
    db.session.add_all([g1, g2, e1, e2])
    db.session.commit()
    print("Seeded!")
