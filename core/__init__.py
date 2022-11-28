from core.config import get_app
from sqlalchemy.ext.declarative import declarative_base 

app = get_app()
BaseModel = declarative_base()
from models import *




@app.get('/')
def root():
    return {'status': 'ok'}