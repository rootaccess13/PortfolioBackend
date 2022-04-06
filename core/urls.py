from django.urls import path
from . views import *
urlpatterns = [
    path('', api, name='api_v1'),
    path('repo/', GithubRepo.as_view({'get': 'get'}), name='repo'),
]
