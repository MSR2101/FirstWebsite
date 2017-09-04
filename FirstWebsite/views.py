from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.template import loader
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from FirstWebsite.models import Merchant, DealProvider, Deals
from FirstWebsite.serializers import MerchantSerializer, DealSerializer


def hello(request):
    sample = "This is your first time"
    text = "<h1>Welcome Online</h1>" + "<h2>%s</h2>" % sample
    return HttpResponse(text)


def article(request):
    return render_to_response("FirstWebsite/hello.html")


def merchant(request):
    html = ''
    allmerchants = Merchant.objects.all()
    for merchants in allmerchants:
        html += "<h2> Merchant Name:" + merchants.merchantDisplayName + "</h2><br>"
    return HttpResponse(html)


def merchant_info(request,user_id):
    return HttpResponse("<h1>Information on Merchant: " + str(user_id) + "</h1>")


#merchantlist/
class Merchantlist(APIView):

    def get(self,request):
        mer = Merchant.objects.all()
        serialize_mer = MerchantSerializer(mer,many=True)
        return Response(serialize_mer.data)

    def post(self,request):
        serialize_mer = MerchantSerializer(data=request.data)
        if serialize_mer.is_valid():
            serialize_mer.save()
            return Response(serialize_mer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialize_mer.errors, status=status.HTTP_400_BAD_REQUEST)



#deallist/
class Deallist(APIView):

    def get(self, request):
        deal = Deals.objects.all()
        serializer_deal = DealSerializer(deal,many=True)
        return Response(serializer_deal.data)


#merchantlist/1
class Merchantlist_1(APIView):

    def get(self, request,mer_id):
        mer = Merchant.objects.get(id=mer_id)
        serialize_mer = MerchantSerializer(mer, many=False)
        return Response(serialize_mer.data)

    def put(self,request, mer_id):
        mer = Merchant.objects.get(pk=mer_id)
        serialize_mer = MerchantSerializer(mer, data=request.data)
        if serialize_mer.is_valid():
            serialize_mer.save()
            return Response(serialize_mer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialize_mer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
