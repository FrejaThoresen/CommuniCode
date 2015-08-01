import gitlab
from django.conf import settings

git = gitlab.Gitlab(settings.GITLAB_HOST, token=settings.GITLAB_TOKEN)
