from random import randint

import pytest
from django.urls import reverse
from pytest_django.asserts import assertQuerysetEqual

from .models import Cartoon


@pytest.mark.urls('cartoon.urls')
def test_login_redirect_to_index(client):
    """Check redirect from login page to index if method == GET"""
    response = client.get('/login/')
    assert response.status_code == 302
    assert response.url == reverse('index')


@pytest.mark.urls('cartoon.urls')
def test_add_cartoon_redirect_to_index(client):
    """Check redirect from add_cartoon page to index if method == GET"""
    response = client.get(reverse('add_cartoon_info'))
    assert response.status_code == 302
    assert response.url == reverse('index')


@pytest.mark.urls('cartoon.urls')
def test_check_content_index(client):
    url = reverse('index')
    response = client.get(url)
    check_text = b'Hello! You need to log in'
    assert response.status_code == 200
    assert check_text in response.content


@pytest.mark.django_db
def test_cartoons_list(client):
    """Check that all records in DB shown in url"""
    response = client.get('/all_info_from_db/')
    cartoons_list = Cartoon.objects.all()
    assertQuerysetEqual(response.context['cartoons'], cartoons_list)


@pytest.mark.django_db
def test_add_cartoon(client):
    """Check added record in DB"""
    year = randint(0, 1500)
    cartoon = Cartoon.objects.create(title='test', year=year, rating=0)
    cartoons_list = Cartoon.objects.all()
    assert cartoon in cartoons_list
