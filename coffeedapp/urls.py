from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'coffeedapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'', include('core.urls')),  
##this includes core.urls but it doesn't work if its under the lines below it.  It has to be first for some reason.

    url(r'^$', include(admin.site.urls)),
    
]
