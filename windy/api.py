from ninja import NinjaAPI

from windspeed.api.routes import wind_router

api = NinjaAPI()

api.add_router("/", wind_router)
