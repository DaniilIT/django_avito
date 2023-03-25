from rest_framework import serializers

from ads.models import User, Location, Ad


class UserListSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        # queryset=Location.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = User
        exclude = ('password',)


class UserDetailSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        # queryset=Location.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = User
        exclude = ('password',)


class UserCreateSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(required=False)
    location = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field='name'
    )

    def is_valid(self, raise_exception=False):
        self._location = self.initial_data.pop('location')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        for loc in self._location:
            loc_obj, _ = Location.objects.get_or_create(name=loc)
            user.location.add(loc_obj)
        # user.save()
        return user

    class Meta:
        model = User
        fields = '__all__'

class UserUpdateSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(required=False)
    location = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field='name'
    )

    def is_valid(self, raise_exception=False):
        self._location = self.initial_data.pop('location')
        return super().is_valid(raise_exception=raise_exception)

    def save(self, **kwargs):
        user = super().save(**kwargs)

        for loc in self._location:
            loc_obj, _ = Location.objects.get_or_create(name=loc)
            user.location.add(loc_obj)
        # user.save()
        return user

    class Meta:
        model = User
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(max_length=20)
    category_name = serializers.CharField(max_length=40)

    class Meta:
        model = Ad
        fields = '__all__'
