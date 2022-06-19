from urllib import request
from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from . models import Accounts
from .serializers import AccountsSerializers

# Create your views here.
def front(request):
    context = { }
    return render(request, "index.html", context)
    
class accountsList(generics.ListAPIView):
    serializer_class = AccountsSerializers

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset= Accounts.objects.all()
        username = self.request.query_params.get('account_name')
        if username is not None:
            queryset = queryset.filter(account_name=username)
        return queryset



   