from django.urls import path
from . import views

app_name = 'instructor'

urlpatterns = [
    path('dashboard/', views.tech_dashboard),
    path('manage_courses/<int:id>/', views.manage_course, name="manage_course"),
    path('manage_lecture/<int:cid>/<int:id>', views.manage_lecture, name="manage_lecture"),
    path('lec_del/', views.lec_del),
    path('add_lecture/', views.add_lecture),
    path('edit_lecture/', views.edit_lecture),
    path('edit_course/', views.edit_course),
    path('profile/', views.up_profile)
]
