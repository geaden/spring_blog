from .base import *

#
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#
# AWS_ACCESS_KEY_ID = get_env_variable('AWS_ACCESS_KEY')
# AWS_SECRET_ACCESS_KEY = get_env_variable('AWS_SECRET_KEY')
# AWS_STORAGE_BUCKET_NAME = ''
#
# S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
# MEDIA_URL = S3_URL

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config(ssl_require=True)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Static assets configuration
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
