from fastapi import FastAPI
from routes.booking_routes import router

app = FastAPI()
app.include_router(router)


from fastapi.staticfiles import StaticFiles

app.mount("/", StaticFiles(directory="static", html=True), name="static")