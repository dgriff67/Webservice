from django.conf.urls import url, include
from .api import Pl1516Resource

pl1516_resource = Pl1516Resource()


urlpatterns = [
    url(r'^', include(pl1516_resource.urls)),
]
