from tastypie.resources import ModelResource
from tpc.models import *
from tastypie.constants import ALL

class DrivesResource(ModelResource):
    class Meta:
        queryset = Drives.objects.all().order_by('-time')
        resource_name = 'all_drives'

class NoticesResource(ModelResource):
	class Meta:
		queryset = Notices.objects.all().order_by('-time')
		resource_name = 'all_notices'
	
