from django.conf.urls import url
from polls.views import polls_list, polls_detail

urlpatterns =  [
    url("polls/", polls_list, name="polls_list"),
    url("polls/<int:pk>/", polls_detail, name="polls_detail"),
]
