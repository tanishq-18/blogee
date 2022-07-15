from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('feed.urls')),
 	path('users/<slug>/', user_views.profile_view, name='profile_view'),
	path('edit-profile/', user_views.edit_profile, name='edit_profile'),
	path('my-profile/', user_views.my_profile, name='my_profile'),
	# path('search_users/', user_views.search_users, name='search_users'),
	path('register/', user_views.register, name='register'),
        path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
        ]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

