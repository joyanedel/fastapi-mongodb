from fastapi import FastAPI
from routes.user.urls import router as userRouter
from routes.skate.urls import router as skateRouter
from routes.guitar.urls import router as guitarRouter

app = FastAPI()

app.include_router(userRouter) #/users
app.include_router(skateRouter) #/skates
app.include_router(guitarRouter) #/guitars