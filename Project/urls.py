from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^professor/(?P<pk>\d+)$', views.ProfessorDetailView.as_view(), name='professor-detail',),
	url(r'^subject/(?P<pk>\d+)$', views.SubjectDetailView.as_view(), name='subject-detail'),


]