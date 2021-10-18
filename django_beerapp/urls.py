from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls'), name="post-urls"),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    # path('review/', include('post.urls')),
    # path('add_review/', include('post.urls')),

]