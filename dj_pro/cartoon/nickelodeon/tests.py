from random import randint

import pytest
from django.urls import reverse

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
    """Check content on page"""
    url = reverse('index')
    response = client.get(url)
    check_text = b'Hello! You need to log in'
    assert response.status_code == 200
    assert check_text in response.content


@pytest.mark.django_db
def test_add_user(client):
    """Check add user"""
    username = b"Test"
    email = 'test' + str(randint(100, 1000)) + '@ithillel.ua'
    response = client.post('/login/', {"username": username, "surname": 'Test23', "email": email})
    assert response.status_code == 200
    assert username in response.content


@pytest.mark.django_db
def test_add_cartoon(client):
    """Check add cartoon"""
    title = b'TestTitle'
    author = b'EtoJa'
    Cartoon.objects.create(title=title, year=2000, author=author, rating=100)
    response = client.get('/all_info_from_db/')
    assert response.status_code == 200
    assert title in response.content
    assert author in response.content
