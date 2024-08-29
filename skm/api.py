from ninja import NinjaAPI
from survey.api import skm_api_router

api = NinjaAPI()


api.add_router('/skm', skm_api_router)