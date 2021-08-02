from django.urls import path
from velorentapp import views

urlpatterns = [
    # ReLoLogout Pages
    path('register/', views.registerPage, name='register', ),
    path('login/', views.loginPage, name='login', ),
    path('logout/', views.logoutUser, name='logout', ),

    # Pages
    path('', views.index, name='index'),
    path('bike', views.bike, name='bike'),
    path('contact', views.contact, name='contact'),


    # Send Message
    path('message/', views.send_message, name='send_message'),
    path('contactmessage/', views.send_contact_message, name='send_contact_message'),

    #  Calculate
    path('calculate', views.calculate, name='calculate'),


]
