from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^(?P<auth_token>\w+)/(?P<trello_model_id>\w+)/$',
        views.api_callback,
        name="trello_callback_url"
    ),
]
