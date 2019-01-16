class DatabaseDevMixin:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'database',
            'USER': 'user',
            'PASSWORD': 'password',
            'HOST': 'host-postgres',
            'PORT': '5432',
        }
    }
