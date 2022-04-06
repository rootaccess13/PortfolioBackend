from rest_framework import serializers
from .models import *


class GithubReposSerializer(serializers.ModelSerializer):
    class Meta:
        model = githubRepos
        fields = ('name', 'description', 'language',
                  'created_at', 'html_url')
