from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext


# Create your views here.

def profile(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/login/')
	
	else:
		user = request.user
		username = user.username
		email = user.email
		first_name = user.first_name
		last_name = user.last_name
		context = {'username': username, 'email': email, 'first_name': first_name, 'last_name': last_name}
		return render_to_response('profile.html', context, context_instance = RequestContext(request))
