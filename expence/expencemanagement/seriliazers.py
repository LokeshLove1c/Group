from rest_framework import serializers
from .models import Group, Users, UserGroup


class GroupSeriliazer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ['gid', 'name', 'description', 'created_by', 'creation_on', 'last_updated_by', 'last_updated_on']



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['uid', 'name', 'email_id', 'phone_no', 'created_by', 'creation_on', 'last_updated_by', 'last_updated_on' ]


class UserGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserGroup
        fields = ['id', 'uid', 'gid']

class UserGroupDataSerializer(serializers.Serializer):
    # uid = UserSerializer()
    gid = GroupSeriliazer()
    class Meta:
        model = UserGroup
        fields = ['id', 'gid']

