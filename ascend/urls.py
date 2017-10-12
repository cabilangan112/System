from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.ascend, name='ascend'),
	url(r'^ascend_student/(?P<pk>\d+)$', views.studentDetailView.as_view(), name=' student',),
	url(r'^ascend_professor/(?P<pk>\d+)$', views.ProfessorDetailView.as_view(), name='professor',),
	url(r'^ascend_grade/(?P<pk>\d+)$', views.ProfessorDetailView.as_view(), name='professor',),
	url(r'^ascend_subject/(?P<pk>\d+)$s', views.SubjectDetailView.as_view(), name='subject'),


]