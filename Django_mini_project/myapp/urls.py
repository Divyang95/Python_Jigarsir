from django.urls import path
from . import views 


urlpatterns = [
    path('',views.index,name="index"),
    path('contact/',views.contact,name='contact'), ##name should match with anchor tag href {% url 'contact'%}
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('change-password/',views.changePassword,name='change-password'),
    path('forgot-password/',views.forgotPassword,name='forgot-password'),
    path('verify-otp/',views.verifyOtp,name='verify-otp'),
    path('new-password/',views.newPassword,name='new-password'), ##here name checks {% url 'new-password' %} come form html <a  href ="{% url 'new-password' %}" 
    path('profile/',views.profile,name='profile'), ##here name checks {% url 'profile' %} come form html <a  href ="{% url 'profile' %}" 
]
