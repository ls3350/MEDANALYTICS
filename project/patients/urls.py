from django.conf.urls import url, include
from patients import views 


urlpatterns = [
    url(r'^$', views.PatientListView.as_view(), name='patient_list' ),
    url(r'^(?P<pk>\d+)$', views.PatientDetailView.as_view(), name='patient_detail'),
    url(r'^create/$', views.PatientCreateView.as_view(), name='patient_create'),
    url(r'^(?P<pk>\d+)/update/$', views.PatientUpdateView.as_view(), name='patient_update'),
    url(r'^(?P<pk>\d+)/delete/$', views.PatientDeleteView.as_view(), name='patient_delete'),
]