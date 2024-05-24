from fastapi import FastAPI
from app.core.model import model
from app.core.database.mysql.database import engine
# from app.features.user.data.model.user import Base

model.Base.metadata.create_all(bind=engine)
app = FastAPI()

