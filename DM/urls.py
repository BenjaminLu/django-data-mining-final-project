from django.conf.urls import patterns, include, url
from django.contrib import admin
from DM.settings import STATIC_ROOT
from DM import views
import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DM.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'excuse.views.home'),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('',
    url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT, 'show_indexes' : False}),
)

handler404 = views.error404
handler500 = views.error500