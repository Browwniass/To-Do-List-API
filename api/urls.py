from api.spectacular.urls import urlpatterns as doc_urls
from django.urls import path, include
from tasks.urls import urlpatterns as tasks_urls


app_name = 'api'

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

urlpatterns += doc_urls
urlpatterns += tasks_urls