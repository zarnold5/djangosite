from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from authenticate.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from brother.models import findUserByEmail
from brother.models import Brother
# Create your views here.

def login_page(request):
	if request.user.is_authenticated(): # why not working??
		return HttpResponseRedirect('/profile/')
	if request.method == 'POST':
		#handle authentication of user
		form = LoginForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			user = findUserByEmail(email)
			if user is None:
				return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
			brother = authenticate(username=user.username, password=password)
			if brother is not None:
				login(request, brother)
				return HttpResponseRedirect('/profile/')
			else:
				return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
		else:
			return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))

	else:
		#user is not submitting the form so show them a blank one...
		form = LoginForm()
		context = {'form': form}
		return render_to_response('login.html', context, context_instance = RequestContext(request))

def logout_request(request):
	logout(request)
	return HttpResponseRedirect("/login/")




