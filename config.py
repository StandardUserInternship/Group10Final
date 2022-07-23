import os
class Config(object):
    SECRET_KEY = os.environ.get("Secret_Key") or "you-will-never-guess"
    
DEBUG = True








