from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('login/', views.login_call),
    path('logout/', views.logout_call),
    path('signup/', views.signup),
    path('contactus/', views.contactus),
    path('student/', include('student.urls')),
    path('instuctor/', include('instructor.urls'))
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
