from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('dashboard/', views.stu_dashboard),
    path('add_cart/<int:id>/', views.add_cart, name='cart'),
    path('delcart/<int:id>/', views.del_cart, name="delcart"),
    path('courses/', views.stu_courses),
    path('profile/', views.up_profile),
    path('cartcalculate/', views.cartcalculate),
    path('filter/', views.filter),
    path('viewcourse/<int:id>/', views.view_course, name="viewcourse"),
    path('viewlecture/<int:cid>/<int:id>', views.view_lecture, name="viewlecture"),
    path('payment_history/', views.payment_history)
]

