from django.urls import path, include
from imageapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('contact', views.contact, name='contact'),
    path('feedback', views.feedback, name='feedback'),
    path('FAQ', views.faq, name='FAQ'),
    path('about', views.about, name='about'),
    path('history', views.history, name='history'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

