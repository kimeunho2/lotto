from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse

class LottoView(View):
    def get(self, request):
        return JsonResponse({"Hello":"world"}) 