from core.config import get_app
from models import *

app = get_app()

@app.get('/')
def root():
    return {'status': 'ok'}
