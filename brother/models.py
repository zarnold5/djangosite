from django.db import models
from django.contrib.auth.models import User 


# Create your models here.
class Brother(models.Model):
	user = models.OneToOneField(User)
	position = models.CharField(max_length = 50)

	def __str__(self):
		return self.user.first_name + ' ' + self.user.last_name

	def getUser(self):
		return self.user

#given an email adress, find the corresponding brother		
def findUserByEmail(emailAddr):
	users = User.objects.all()
	for user in users:
		if user.email == emailAddr:
			return user
	return None



