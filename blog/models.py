from django.db import models

# Create your models here.
class Article(models.Model):
    # 文章ID
    article_id = models.AutoField(primary_key=True)
    # 文章标题
    title = models.TextField()
    # 文章摘要
    brief_content = models.TextField()
    # 文章内容
    content = models.TextField()
    # 文章发表日期
    publish_date = models.DateTimeField(auto_now=True)
