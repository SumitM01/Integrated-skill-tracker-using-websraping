from django.urls import path
from . import views

urlpatterns = [
    path('',views.courses,name='courses-page'),
    path('update_status/',views.question_status_update,name='status-update'),
]
