# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jc!02(v1r1*=%8fjs5-@_h*fhp=g_$&tx9dy*sg_jv&y$o!1($!g'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
DEBUG = True

# '*' for all allowed hosts
ALLOWED_HOSTS = ['*','10.148.72.193']

# RDS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bpdb',
        'HOST': 'devbpdb.cjijufb0sfjq.us-west-2.rds.amazonaws.com',
        'USER': 'bpdbuser',
        'PASSWORD': 'Blaize12#',
        'PORT': '5432',
    }
}

# Email Config
EMAIL_HOST = 'smtp.office365.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'bpdb@blaize.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
