import pytest
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from ..models import Post


@pytest.mark.django_db()
def test_title_create():
    User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    date_created = timezone.now()
    article = Post.objects.create(title='article1',
                                  author_id=1,
                                  content='Content1',
                                  date_created=date_created)

    assert article.title == 'article1'
    assert article.content == 'Content1'
    assert article.date_created == date_created

