release: python manage.py migrate
web: gunicorn uts.wsgi

# Activate Django-Heroku in deployment
import django_heroku
django_heroku.settings(locals())

# Simplified static file serving .
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'