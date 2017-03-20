DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'streamchats2',
        'USER': 'dev',
        'PASSWORD': '123456',
        }
}

SECRET_KEY = 'PUT_SOME_RANDOM_STRING_HERE'