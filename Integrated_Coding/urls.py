from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from users.views import error_404_view

handler404 = 'users.views.error_404_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('users.urls')),
    path('contest/',include('contest.urls')),
    path('courses/',include('courses.urls')),
    path('',include('coding_profile.urls')),
    
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='index.html'),name='logout'),
    path('reset-password/',
        auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
        name='reset_password'),
    path('password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('password-reset-complete',
        auth_views.PasswordResetCompleteView.as_view(template_name='index.html'),
        name='password_reset_complete'),
    path('verification/', include('verify_email.urls')),
    path('password_change',auth_views.PasswordChangeView.as_view(template_name='change_password.html', success_url = 'home/'),name='change-password'),
    # path('',include('import_excel_db.urls')),
]
 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

