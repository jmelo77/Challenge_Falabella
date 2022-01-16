import os

class Common(object):
    '''
    Configuration base, for all enviroments.
    '''
    DEBUG = os.environ.get('DEBUG', False)
    VERSION = '1.0'
    PATENT_BACKEND_PREFIX = 'patent-api'

class Dev(Common):
    DEBUG = True

class Stg(Common):
    DEBUG = os.environ.get('DEBUG', True)

class Prd(Common):
    DEBUG = os.environ.get('DEBUG', False)
