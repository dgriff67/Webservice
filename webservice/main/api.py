from tastypie.resources import ModelResource
from tastypie.constants import ALL
from .models import Pl1516

class Pl1516Resource(ModelResource):
    class Meta:
        queryset = Pl1516.objects.all()
        resource_name = 'Pl1516'
        filtering = {
            "hometeam" : ALL
        }