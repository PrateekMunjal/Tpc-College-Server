from django.conf.urls import patterns, include, url
from tpc import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib import admin
from tpc.api import *

drives_Resource = DrivesResource()
notices_Resource = NoticesResource()

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'placementCell.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^$',views.home),    
	url(r'^about/$',views.about),
	url(r'^post/$',views.post),
	url(r'^postDrive/',views.postDrive),
	url(r'^allDrives/$',views.allDrives),
	url(r'^api/',include(drives_Resource.urls)),
	url(r'^notices_api/',include(notices_Resource.urls)),
	url(r'^mobile/',views.mobile),
	url(r'^edit/$',views.edit),
	url(r'^update/(?P<company_name>[\w ()-/.]+)',views.updateCompany),
	url(r'^allRegistrations/$',views.allRegistrations),
	url(r'^company/(?P<company_name>[\w ()-/.]+)',views.companyWiseRegistration),
	url(r'^notice/$',views.notice),
)
urlpatterns += staticfiles_urlpatterns()
