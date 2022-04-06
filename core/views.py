from django.shortcuts import render
import os
from matplotlib.style import context
import requests

from django.shortcuts import render
from django.contrib.auth.models import User
from . import serializers
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from . models import githubRepos
import json
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed
from rest_framework_simplejwt.backends import TokenBackend
from django.core.exceptions import ValidationError


def api(request):
    github_url = "https://api.github.com/user/repos"
    github_token = "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"
    print(github_token)
    headers = {'Authorization': 'token ' + github_token}
    response = requests.get(github_url, headers=headers)
    print(response.json())
    context = {
        'repos': response.json(),
    }
    return render(request, 'core/api.html', context)


class GithubRepo(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = githubRepos.objects.all()
    serializer_class = serializers.GithubReposSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        list = self.queryset.all()
        serializer = serializers.GithubReposSerializer(list, many=True)
        return Response(serializer.data)
