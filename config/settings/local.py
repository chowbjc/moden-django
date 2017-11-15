from .base import *
SECRET_KEY = env('DJANGO_SECRET_KEY', default='z7z=$bmv@y-6v1w&4l!2cl1c!^+1^ljuk&r_h%ybfozxv%^uu1')
DEBUG = env.bool('DJANGO_DEBUG', default=True)
