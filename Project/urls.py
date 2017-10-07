from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^students/', views.studentListView.as_view(), name='student'),
]