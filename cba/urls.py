from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.view, name='view'),
	url(r'^student_cba/(?P<pk>\d+)$', views.studentDetailView.as_view(), name=' studentdetail',),
	url(r'^professor_cba/(?P<pk>\d+)$', views.ProfessorDetailView.as_view(), name='professordetail',),
	url(r'^grade_cba/(?P<pk>\d+)$', views.ProfessorDetailView.as_view(), name='professordetail',),
	url(r'^subject_cba/(?P<pk>\d+)$', views.SubjectDetailView.as_view(), name='subjectdetail'),


]