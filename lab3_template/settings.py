# PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lab4_learning_django',
        'USER': 'postgres',
        'PASSWORD': 'Tuandayne5047#$',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

INSTALLED_APPS = (
    'related_objects',
)

SECRET_KEY = 'SECRET KEY for this Django Project'
