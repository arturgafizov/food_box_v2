
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

    for food in foods:
        d = {}
        d['name'] = food['name']
        d['about'] = food['about']
        d['weight_grams'] = food['weight_grams']
        d['price'] = food['price']
        result.append(d)

    return Response(result)



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
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



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

    return Response(result)



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
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


