from django.conf import settings
from django.contrib.auth.models import User

class FenixEduAuthenticationBackend(object):
	def add_info_to_session(self, request, fenixeduUser):
		request.session['access_token'] = fenixeduUser.access_token
		request.session['refresh_token'] = fenixeduUser.refresh_token

	def authenticate(self, request, client, code=None):
		if code is not None:
			fenixeduUser = client.get_user_by_code(code)
			person = client.get_person(fenixeduUser)
			username = person['username']
			try:
				user = User.objects.get(username=username)
			except User.DoesNotExist:
			# The user is not registered in the application yet
				name = person['name']
				name_parts = name.split(' ')
				first_name = name_parts[0]
				last_name = ''
				if len(name_parts) > 1:
					last_name = name_parts[len(name_parts) - 1]
				user = User(username=username, first_name=first_name, last_name=last_name)
				user.save()
			self.add_info_to_session(request, fenixeduUser)
			return user
		else:
			return None

	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None