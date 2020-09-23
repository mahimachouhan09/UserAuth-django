from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views
from django.contrib.auth.views import(
  PasswordResetView,
  PasswordResetConfirmView, PasswordResetDoneView,
  PasswordResetCompleteView)

app_name = 'UserLogin'
urlpatterns = [
  path('', views.index, name='index'),
  path('signup/', views.signup, name='signup'),
  path('login/', views.view_login, name='login'),
  path('logout/', views.view_logout, name='logout'),
  path('change_password/', views.change_password, name='change_password'),
  # path('password-reset/', auth_views.PasswordResetView.as_view(
  #   template_name='account/password_reset.html'), name='password_reset'),

  # path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
  #   template_name='account/password_reset_done.html'),
  #   name='password_reset_done'),

  # path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
  #   template_name='account/password_reset_confirm.html'),
  #   name='password_reset_confirm'),

  # path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
  #   template_name='account/password_reset_complete.html'), name='password_reset_complete'),

  path('update-profile/', views.update_profile, name='profile_update'),
]
