# logic

from fastapi import FastAPI
from routes import base , data 
# makes the app variables to the whole system


app = FastAPI()
app.include_router(base.base_router)
app.include_router(data.data_router)