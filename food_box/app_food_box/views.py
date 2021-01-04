# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests


@api_view(http_method_names=['GET'])
def food_list(request):
    link_food = requests.get('https://stepik.org/media/attachments/course/73594/foodboxes.json')
    foods = link_food.json()
    result = []
    result1 = []
    if request.query_params:
        min_price = request.query_params.get('min_price')
        min_weight = request.query_params.get('min_weight')
        if not min_price and not min_weight:
            return Response(result)
        if min_price:
            for food in foods:
                if food['price'] >= int(min_price):
                    result1.append(food)
            for food1 in result1:
                d1 = {}
                d1['name'] = food1['name']
                d1['about'] = food1['about']
                d1['weight_grams'] = food1['weight_grams']
                d1['price'] = food1['price']
                result.append(d1)
            if result:
                return Response(result)
            else:
                result = foods
        if min_weight:
            for food in foods:
                if food['weight_grams'] >= int(min_weight):
                    result1.append(food)
            for food1 in result1:
                d1 = {}
                d1['name'] = food1['name']
                d1['about'] = food1['about']
                d1['weight_grams'] = food1['weight_grams']
                d1['price'] = food1['price']
                result.append(d1)
            if result:
                return Response(result)
            else:
                result = foods

    for food in foods:
        d = {}
        d['name'] = food['name']
        d['about'] = food['about']
        d['weight_grams'] = food['weight_grams']
        d['price'] = food['price']
        result.append(d)

    if result:
        return Response(result)
    elif link_food.status_code == 404:
        return Response(status=status.HTTP_404_NOT_FOUND)
    elif link_food.status_code == 408:
        return Response(status=status.HTTP_408_REQUEST_TIMEOUT)


@api_view(http_method_names=['GET'])
def food_detail(request, pk):
    link_food = requests.get('https://stepik.org/media/attachments/course/73594/foodboxes.json')
    foods = link_food.json()
    d = {}
    response = None
    for food in foods:
        if food['inner_id'] == pk:
            d['name'] = food['name']
            d['about'] = food['about']
            d['weight_grams'] = food['weight_grams']
            d['price'] = food['price']
            response = d

    if response:
        return Response(response)
    elif link_food.status_code == 404:
        return Response(status=status.HTTP_404_NOT_FOUND)
    elif link_food.status_code == 408:
        return Response(status=status.HTTP_408_REQUEST_TIMEOUT)


@api_view(http_method_names=['GET'])
def recipient_list(request):
    link_recipient = requests.get('https://stepik.org/media/attachments/course/73594/recipients.json')
    recipients = link_recipient.json()
    result = []

    for recipient in recipients:
        d = {}
        d = recipient['info']
        d['phoneNumber'] = recipient['contacts']['phoneNumber']
        result.append(d)

    if result:
        return Response(result)
    elif link_recipient.status_code == 404:
        return Response(status=status.HTTP_404_NOT_FOUND)
    elif link_recipient.status_code == 408:
        return Response(status=status.HTTP_408_REQUEST_TIMEOUT)


@api_view(http_method_names=['GET'])
def recipient_detail(request, bk):
    link_recipient1 = requests.get('https://stepik.org/media/attachments/course/73594/recipients.json')
    recipients1 = link_recipient1.json()
    d = {}

    response = None
    for recipient in recipients1:
        if recipient['id'] == bk:
            d = recipient['info']
            d['phoneNumber'] = recipient['contacts']['phoneNumber']
            response = d

    if response:
        return Response(response)
    elif link_recipient1.status_code == 404:
        return Response(status=status.HTTP_404_NOT_FOUND)
    elif link_recipient1.status_code == 408:
        return Response(status=status.HTTP_408_REQUEST_TIMEOUT)
