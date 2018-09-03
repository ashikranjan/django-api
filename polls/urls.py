from django.conf.urls import url
from polls.apiviews import PollList, PollDetail

urlpatterns =  [
    url("polls/", PollList.as_view(), name="polls_list"),
    url("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
]
