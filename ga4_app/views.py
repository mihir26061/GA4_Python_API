from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from ga4_project.services import (
    get_total_users,
    get_month_start_end,
)



class GA4ServiceView(APIView):
    
    def get(self,request):
        return Response({'status': 'success'})
    
    def post (self, request):

        start_date, end_date = get_month_start_end()
        all_users = get_total_users(start_date, end_date)

        if all_users.get('row_count'):
            # All records/rows.
            all_users['rows']
            print("All users", all_users)
