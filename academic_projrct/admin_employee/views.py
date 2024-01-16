from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def empl_mng(request):
    return render(request, 'emp_mng.html')