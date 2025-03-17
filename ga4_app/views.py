from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse



class GA4ServiceView(APIView):
    
    def get(self,request):
        return Response({'status': 'success'})
    
    def post (self, request):
        pass