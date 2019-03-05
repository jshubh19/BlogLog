from django.conf.urls import url,include
from django.contrib import admin
from users import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from django.views.generic import TemplateView

app_name='users'


urlpatterns=[
    url(r'^register/$',views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),

    #these are django built-in views which we use directly by  importing them

    # user login and logout urls
    url(r'^login/$',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

    #user password change urls with old password
    url(r'^password-change/$', auth_views.PasswordChangeView.as_view(template_name='password_change_form.html',success_url=reverse_lazy('users:password_change_done')),
        name='password_change'),
    url(r'^password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),

    # password reset urls
    url(r'^password-reset/$', auth_views.PasswordResetView.as_view(template_name='password_reset.html',success_url=reverse_lazy('users:password_reset_done')),
        name='password_reset'),
    url(r'^password-reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,23})/$', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^password-reset/complete/$', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),



    # DIRECTLY INCLUDE password reset url with built in template of Django adminstration
    #url(r'^',include('django.contrib.auth.urls')),
]