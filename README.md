fenixedu_django
===============

FenixEdu authentication backend for django framework.
If you want to develop an app using django and use FenixEdu API to authenticate your
users you can use this backend instead of writing all authentication code yourself ;)

If you don't know what the hell is FenixEdu check it out

<a href="http://fenixedu.org/">FenixEdu.org</a>

<a href="http://fenixedu.org/dev/">FenixEdu Developer</a>




## Installation

* If you don't have fenixedu installed, install it first

```
pip install fenixedu
```

* Install fenixedu django

```
pip install fenixedu-django
```

## Usage

* Add the FenixEdu authentication backend to your settings.py

```python
AUTHENTICATION_BACKENDS = (
	'fenixedu.authentication.backend.FenixEduAuthenticationBackend',
)
```

* Import fenixedu

```python
import fenixedu
```

* Instatiatie the FenixEdu Client

** See how here

<a href="https://github.com/samfcmc/fenixedu-python-sdk">FenixEdu Python SDK repository</a>

```python
client = fenixedu.FenixEduClient(...)
```

* Add a link to the authentication url in your web page

** Example: Show the authentication url in index.html

*** In views.py

```python
def index(request):
	context = {'auth_url': client.get_authentication_url()}
	return render(request, 'index.html', context)
```

*** In index.html

```
<a href="{{ auth_url }}">Login</a>
```

* After the user logged in and authorized your application he will be redirected to the redirect URL,
which will have a code parameter

* In the view that will receive the code do the following:

```python
code = request.GET.get('code', None)
if code is not None and not request.user.is_authenticated():
	user = authenticate(request=request, client=client, code=code)
	if user is not None:
		login(request, user)

```

* Now your user is authenticated.

* If you want to use FenixEdu API endpoints of private scope you can get the user object from the request

```python
from fenixedu.authentication import users
...
user = users.get_fenixedu_user(request)
# Example: get person
person = client.get_person(user=user)
```

Any bug, request or anything else just open an issue ;)
