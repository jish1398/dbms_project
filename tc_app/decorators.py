from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect,JsonResponse

def login_required(view_func):
	def login_check(request, test_number = 0):
		if 'user' in request.session:
			try:
				return view_func(request, test_number)
			except:
				return view_func(request)
		else :
			return HttpResponseRedirect('/tc/login')
	return login_check