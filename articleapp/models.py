from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)  # related_name: User에서 aricle 접근시 사용
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)
    created_at = models.DateField(auto_created=True, null=True)





