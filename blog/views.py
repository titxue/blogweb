from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from blog.models import Article


def article_content(request):
    article = Article.objects.all()[0]
    article_id = article.article_id
    title = article.title
    brief_content = article.brief_content
    content = article.content
    publish_date = article.publish_date
    return_str = '编号：%s，标题：%s，' \
                 '摘要：%s，内容：%s，发表日期：%s' % (
                     article_id,
                     title,
                     brief_content,
                     content,
                     publish_date
                 )
    return HttpResponse(return_str)


# blog首页
def get_index_page(request):
    all_article = Article.objects.all()
    return render(request, 'blog/index.html',
                  {
                      'articles': all_article
                  }
                  )


# 文章内容
def get_detail_page(request, article_id):
    all_article = Article.objects.all()
    curr_article = None
    previous_index = 0
    next_index = 0
    previous_article = None
    next_article = None
    for index, article in enumerate(all_article):
        if index == 0:
            previous_index = 0
            next_index = index + 1
        elif index == len(all_article) - 1:
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1
        if article.article_id == article_id:
            curr_article = article
            previous_article = all_article[previous_index]
            next_article = all_article[next_index]
            break

    section_list = curr_article.content.split('\n')
    return render(request, 'blog/detail.html',
                  {
                      'curr_article': curr_article,
                      'sections': section_list,
                      'previous_article': previous_article,
                      'next_article': next_article,
                  }
                  )
