# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!+l^8jg7j9x=jhknxdml=#815qy0v03agvzt4ik))%#%%f+u4_'


DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root',
        'PASSWORD': 'BigRock',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
