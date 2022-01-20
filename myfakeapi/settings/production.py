from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['myfakeapibackend.herokuapp.com']


# postgresql connector sql
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'dfshatck2f1vhc',
       'USER': 'borbziwezgorqo',
       'PASSWORD': '57a36d4a0bfc90b4dd498489e847cba336da499e77d68f37fd889489c97e9b5e',
       'HOST': 'ec2-3-222-24-200.compute-1.amazonaws.com',
       'PORT': '5432',
   }
}
