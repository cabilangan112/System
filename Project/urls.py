from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^student/(?P<pk>\d+)$', views.studentDetailView.as_view(), name=' student-detail',),
	url(r'^professor/(?P<pk>\d+)$', views.ProfessorDetailView.as_view(), name='professor-detail',),
	url(r'^grade/(?P<pk>\d+)$', views.ProfessorDetailView.as_view(), name='professor-detail',),
	url(r'^subject/(?P<pk>\d+)$', views.SubjectDetailView.as_view(), name='subject-detail'),


]