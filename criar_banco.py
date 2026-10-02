from fakepinterest import database, app
from fakepinterest.models import Foto

with app.app_context():
    Foto.query.delete()
    database.session.commit()