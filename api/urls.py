from api.spectacular.urls import urlpatterns as doc_urls
from django.urls import path, include
from users.urls import urlpatterns as users_urls


app_name = 'api'

urlpatterns = [
    path('auth/', include('djoser.urls.jwt')),
]

urlpatterns += doc_urls
urlpatterns += users_urls