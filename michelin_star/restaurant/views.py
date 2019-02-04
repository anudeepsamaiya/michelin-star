import requests

from rest_framework.views import APIView
from rest_framework import renderers
from rest_framework.response import Response


ZOMATO_REQUEST_KEY = "9296452f72997211acc2cd9dcc772b2b"

class ZOMATO_ENDPOINT:
    base = "https://developers.zomato.com/api/v2.1"
    search = base + "/search"

class RestaurantList(APIView):
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer,)
    template_name = 'restaurant/restaurant_list.html'

    def get(self, request, *args, **kwargs):
        params = request.query_params
        headers = {'user-key': ZOMATO_REQUEST_KEY, 'content-type':'application/json'}
        response = requests.get(ZOMATO_ENDPOINT.search, headers=headers,
                params=params)
        return Response(response.json())
