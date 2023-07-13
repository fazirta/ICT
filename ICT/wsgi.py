import os

from django.core.wsgi import get_wsgi_application

from whitenoise import WhiteNoise

from pathlib import Path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ICT.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=str(Path(__file__).resolve().parent.parent) + "/static")
