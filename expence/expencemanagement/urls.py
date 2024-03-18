
from django.urls import path, re_path
from .views import GroupList, UserList, UserGroup

urlpatterns = [
    path('groups/', GroupList.as_view(), name='groupL_list'),
    path('users/', UserList.as_view(), name='user_list'),
    re_path(r'user/(?P<user_id>[0-9])/groups/', UserGroup.as_view(), name='user_group'),
    # path('group/expences', views.as_view(), name = 'group_expences'),
]