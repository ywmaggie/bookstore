from django.conf.urls import patterns, include, url
from project import views
import os
from django.contrib.auth.views import login, logout
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
	('^$',views.homepage),
	(r'homepage/',views.homepage),	
	(r'^admin/', include(admin.site.urls)),
	(r'login/',views.login),
	(r'^accounts/logout/$', logout,{'next_page':'/homepage/'}),
	(r'manage/',views.manage),

	(r'^inventory/',views.inventory),
	(r'^search/',views.search),
	(r'^edit/',views.edit),
	(r'^sell/',views.sell),
	
	(r'^buy/',views.buy),
	(r'^import/',views.buyin),
	(r'^pay/',views.pay),
	(r'^cancel/',views.cancel),
	(r'^add/',views.add),	
	
	(r'^bill/',views.checkbill),


 (r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates/images/')}),
    (r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates/css/')}),
   (r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates/js/')}),
    
)

