import requests

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import status

from restaurant.models import Restaurant
from restaurant.serializers import RestaurantSerializer

ZOMATO_REQUEST_KEY = "9296452f72997211acc2cd9dcc772b2b"

class ZOMATO_ENDPOINT:
    root = "https://developers.zomato.com/api/v2.1"
    search = root + "/search"
    restaurant = root + "/restaurant"


class RestaurantList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    renderer_classes = (renderers.TemplateHTMLRenderer, renderers.BrowsableAPIRenderer, renderers.JSONRenderer,)
    template_name = 'restaurant/restaurant_list.html'

    def get(self, request, *args, **kwargs):
        params = request.query_params
        headers = {'user-key': ZOMATO_REQUEST_KEY, 'content-type':'application/json'}
        response = requests.get(ZOMATO_ENDPOINT.search, headers=headers,
                params=params)
        return Response({'object': response.json()})


class RestaurantDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    renderer_classes = (renderers.TemplateHTMLRenderer, renderers.BrowsableAPIRenderer, renderers.JSONRenderer,)
    serializer_class = RestaurantSerializer
    template_name = 'restaurant/restaurant.html'

    def get(self, request, *args, **kwargs):
        params = request.query_params.copy()
        params.update(kwargs)
        headers = {'user-key': ZOMATO_REQUEST_KEY, 'content-type':'application/json'}
        response = requests.get(ZOMATO_ENDPOINT.restaurant, headers=headers,
                params=params)

        res_id = kwargs.get('res_id')
        obj = res_id and Restaurant.objects.filter(aggregator_id=res_id).last()
        user_data = None
        if obj:
            serializer = RestaurantSerializer(obj)
            user_data = serializer.data

        return Response({'object': response.json(), 'user_data': user_data})

    def post(self, request, *args, **kwargs):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'object':{}}, status=status.HTTP_400_BAD_REQUEST)
