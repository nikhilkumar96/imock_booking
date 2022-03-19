from sanic.response import json
from sanic.views import HTTPMethodView

from constant import *


class BookingView(HTTPMethodView):

    async def get(self, request):
        parser = ""
        response = ""
        return json(response)

    async def post(self, request):
        parser = ""
        response = ""
        return json(response)

    async def patch(self, request):
        parser = ""
        response = ""
        return json(response)

    async def delete(self, request):
        parser = ""
        response = ""
        return json(response)
