'''System Module'''
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),
    path('members/', include('members.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = "django_beerapp.views.page_not_found_view"
handler500 = "django_beerapp.views.my_custom_error_view"
handler403 = 'django_beerapp.views.error_403'
handler400 = "django_beerapp.views.my_custom_bad_request_view"
