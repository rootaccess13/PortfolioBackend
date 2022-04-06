from django.contrib import admin
from . models import githubRepos


@admin.register(githubRepos)
class githubReposAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'language',
                    'created_at', 'html_url')
