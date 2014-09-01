import fenixedu

def get_fenixedu_user(request):
	access_token = request.session.get('access_token')
	refresh_token = request.session.get('refresh_token')
	user = fenixedu.User(access_token=access_token, refresh_token=refresh_token)
	return user