import pytest
import django
from django.contrib.auth.models import User

django.setup()

@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    print(User.objects.count() == 1    )
    assert User.objects.count() == 1    


@pytest.mark.django_db
def test_my_user():
    me = User.objects.get(username='lgonzalez')
    assert me.is_superuser