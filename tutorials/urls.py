from django.urls import path
from tutorials import views as tutorials_views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import reverse
import pytest

urlpatterns = [
    path('', tutorials_views.index.as_view(), name='home'),
    path('api/tutorials/', tutorials_views.tutorial_list),
    path('api/tutorials/<int:pk>/', tutorials_views.tutorial_detail),
    path('api/tutorials/published/', tutorials_views.tutorial_list_published)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


@pytest.fixture 
def test_user(db, django_user_model):     
    django_user_model.objects.create_user(username="test_username", password="test_password")
    return "test_username", "test_password"   # this returns a tuple

def test_login_user(client, test_user):
    test_username, test_password = test_user  # this unpacks the tuple     
    login_result = client.login(username=test_username, password=test_password)     
    assert login_result == True