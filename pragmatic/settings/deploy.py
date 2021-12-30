from .base import *
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)


# reading .env file
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)
SECRET_KEY = env('SECRET_KEY')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'pi',
        'PASSWORD': 'billyiscute',
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}