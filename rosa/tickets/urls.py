from django.conf.urls import url 
from tickets import views
 
urlpatterns = [ 
    url(r'^api/tickets$', views.ticket_list),
    url(r'^api/tickets/(?P<pk>[0-9]+)$', views.ticket_detail),
    url(r'^api/tickets/checkedin$', views.ticket_list_checkedin)
]
