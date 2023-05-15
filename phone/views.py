from django.shortcuts import render
import datetime
from phone.models import Product




def main_page_view(request):
    if request.method == 'GET':
        return render(request,'layouts/index.html')


def phone_view(request):
    if request.method == 'GET':
        phones = Product.objects.all()
        contex = {
            'phones':phones
        }
        return render(request,'phones/phones.html',context=contex)