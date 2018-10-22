from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
	return render(request,'tc_app/index.html')

@csrf_exempt
def get_element(request):
	name=request.POST.get("name","")
	admission=request.POST.get("admission","")
	email=request.POST.get("email","")
	password=request.POST.get("pass","")
	print(str(email)+" "+str(name)+" "+str(admission)+" "+str(password))
	return render(request,'tc_app/index.html')	
				