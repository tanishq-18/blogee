from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('feed.urls')),
	path('users/', user_views.users_list, name='users_list'),
	path('users/<slug>/', user_views.profile_view, name='profile_view'),
	path('edit-profile/', user_views.edit_profile, name='edit_profile'),
	path('my-profile/', user_views.my_profile, name='my_profile'),
	path('search_users/', user_views.search_users, name='search_users'),
	path('register/', user_views.register, name='register'),
        path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
        path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
        path('password-reset/done/', auth_views.PasswordResetView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
        path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
        path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

