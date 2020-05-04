# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jc!02(v1r1*=%8fjs5-@_h*fhp=g_$&tx9dy*sg_jv&y$o!1($!g'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
DEBUG = True

# '*' for all allowed hosts
ALLOWED_HOSTS = ['*']

# RDS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'awsdemo_db',
        'HOST': 'django-aws-demo.cvvl8zxdxncv.us-west-1.rds.amazonaws.com',
        'USER': 'awsdemouser',
        'PASSWORD': 'awsdemouser',
        'PORT': '5432',
    }
}

# Email Config
EMAIL_HOST = 'smtp.office365.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'acme@gmail.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
