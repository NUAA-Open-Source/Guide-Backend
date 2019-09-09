from django.http import HttpResponse
import json
from .models import Card

# Create your views here.
def get_all(request):
    cards = Card.objects.order_by('-rate')
    output = []
    for card in cards:
        card_json = {}
        card_json["name"] = card.name
        card_json["introduction"] = card.introduction
        card_json["author"] = card.author
        card_json["url"] = card.url
        output.append(card_json)
    return HttpResponse(json.dumps(output))

