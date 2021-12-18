from rest_framework import serializers, viewsets
from rest_framework.response import Response
import requests
from rest_framework.views import APIView
from .models import Data
from .serializer import DataSerializer
from rest_framework.response import Response
from datetime import datetime
import time
from ..app.settings import API_KEY

class DataAPIView(APIView):
  serializer_class = DataSerializer

  def get_querysets(self):
    return Data.objects.all()

  def get(self, request, *args, **kwargs):
    data = self.get_querysets()
    serializer = DataSerializer(data , many= True)
    return Response(serializer.data)

  def post(self, request, *args, **kwargs):
    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey={API_KEY}"
    api_request = requests.get(url)

    try:
      api_request.raise_for_status()
      data = api_request.json()
    except:
      return None

    data_api = data
    print("Force Fetching Data" , datetime.now())
    if data_api is not None:
      try:
        data_api = data_api['Realtime Currency Exchange Rate']
        new_data = Data.objects.create( exchange_rate=data_api['5. Exchange Rate'].replace("Z","").replace("T"," "),
                                  last_refreshed=data_api['6. Last Refreshed'] , 
                                  bid_price= data_api['8. Bid Price'], 
                                  ask_price= data_api['9. Ask Price'] )

        serializer = DataSerializer(new_data)
        serializer.save()
      except:
        pass
    return Response(serializer.data)


# @api_view(['POST',])
# def api_create(request):
  
#   url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey={API_KEY}"
#   api_request = requests.get(url)

#   try:
#     api_request.raise_for_status()
#     data = api_request.json()
#   except:
#     return None

#   data_api = data
#   print("Fetching Data" , datetime.now())
#   if data_api is not None:
#     try:
#       data_api = data_api['Realtime Currency Exchange Rate']
#       new_data = Data.objects.create( exchange_rate=data_api['5. Exchange Rate'].replace("Z","").replace("T"," "),
#                                 last_refreshed=data_api['6. Last Refreshed'] , 
#                                 bid_price= data_api['8. Bid Price'], 
#                                 ask_price= data_api['9. Ask Price'] )

#       serializer = DataSerializer(new_data)
#       serializer.save()
#     except:
#       pass
#   return Response(serializer.data)


class DataViewset(viewsets.ModelViewSet):
  serializer_class = DataSerializer

  def get_queryset(self):
    data = Data.objects.all()
    return data

  def _get_data_api(self):
    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey={API_KEY}"
    api_request = requests.get(url)

    try:
      api_request.raise_for_status()
      return api_request.json()
    except:
      return None
    
  
  def save_data_api(self):
    data_api = self._get_data_api()
    print("Fetching Data" , datetime.now())
    if data_api is not None:
      try:
        data_api = data_api['Realtime Currency Exchange Rate']
        data_api = Data.objects.create( exchange_rate=data_api['5. Exchange Rate'].replace("Z","").replace("T"," "),
                                        last_refreshed=data_api['6. Last Refreshed'] , 
                                        bid_price= data_api['8. Bid Price'], 
                                        ask_price= data_api['9. Ask Price'] )
        data_api.save()
      except:
        pass
  
  def create(self):
    data_api = self._get_data_api()
    print("Fetching Data" , datetime.now())
    if data_api is not None:
      try:
        data_api = data_api['Realtime Currency Exchange Rate']
        new_data = Data.objects.create( exchange_rate=data_api['5. Exchange Rate'].replace("Z","").replace("T"," "),
                                last_refreshed=data_api['6. Last Refreshed'] , 
                                bid_price= data_api['8. Bid Price'], 
                                ask_price= data_api['9. Ask Price'] )

        serializer = DataSerializer(new_data)
        serializer.save()
      except:
        pass
    return Response(serializer.data)

