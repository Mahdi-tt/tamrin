from mysite.settings import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%0z$4!^er4as49f(+f%qdh(^c&!+$ddob9$6#_f5cq%pv%4)@l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []




#capcha
# https://pylessons.com/django-recaptcha
RECAPTCHA_PUBLIC_KEY = '6Lcp9ZsqAAAAALjIpdP2F4Q2nfLBdFxOXb3vXw7R'
RECAPTCHA_PRIVATE_KEY = '6Lcp9ZsqAAAAANPakRQQjU7wqo2n4hAiNLTrRQhT' 
 

#sites
SITE_ID = 2


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
}

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]
STATIC_ROOT= BASE_DIR/'static'
MEDIA_ROOT = BASE_DIR / 'media'
