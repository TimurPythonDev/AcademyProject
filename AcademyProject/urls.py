from django.contrib import admin
from django.urls import path
# Static modules
from django.conf import settings
from django.conf.urls.static import static
# views.py modules
from app.views import *

urlpatterns = [
    # About PATH
    path('admin/', admin.site.urls),
    path('base',Home,name='base'),
    path('index',Index,name='index'),
    path('project/<str:pk>/',Course, name="project"),

    # Login Logout
    path('login_page',LOGINPAGE,name='login_page'),
    path('Login', Login, name='Login'),
    path('Logout', Logout, name='Logout'),

    # Send Message ADMIN
    path('inbox',inboxPage, name="inbox"),
    path('message/<str:pk>/',messagePage, name="message"),

    # Add Course ADMIN
    path('add-course/',addProject, name="add-course"),
    path('edit-course/<str:pk>/',editProject, name="edit-course"),
    path('course',Course,name='course'),

    # All PATH
    path('about',About,name='about'),
    path('form',RegisteForm,name='register'),
    path('contact',Contact,name='contact'),

# Media settings
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
