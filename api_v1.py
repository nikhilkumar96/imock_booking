from sanic import Blueprint

from constant import *
from views.booking_view import BookingView

API_VERSION = 'v1'


def setup_api(app):
    api_prefix = f'/{SERVICENAME.lower()}/{API_VERSION}'
    api_v1 = Blueprint(API_VERSION, url_prefix=api_prefix)

    api_v1.add_route(BookingView.as_view(), '/register', strict_slashes=False)
    app.blueprint(api_v1)
