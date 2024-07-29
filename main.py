from App.dependencies import app
from App.routers.users import router as router_app

app.include_router(router_app)
