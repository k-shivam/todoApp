from django.conf.urls import url

from .views import index, remove

urlpatterns=[
    url(r'^$', index, name="todo"),
    url(r'del/(?P<item_id>\d+)', remove, name='del'),

]