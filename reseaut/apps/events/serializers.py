from rest_framework import serializers
from apps.profiles.serializers import ProfileSerializer
from .models import Event,Comment

class EventSerializer(serializers.ModelSerializer):

    author = ProfileSerializer(read_only=True)

    description = serializers.CharField(required=True)

    event_name = serializers.CharField(required=True)

    event_date = serializers.DateField(required=True)

    event_time = serializers.TimeField(required=True)

    location = serializers.CharField(required=True)

    image = serializers.SerializerMethodField()

    slug = serializers.SlugField(required=False)

    createdAt = serializers.SerializerMethodField(method_name="get_created_at")

    updateAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:

        model = Event

        fields = (
            'author',
            'description',
            'event_name',
            'event_date',
            'event_time',
            'location',
            'image',
            'slug',
            'createdAt',
            'updateAt'
        )

    def create(self, validated_data):
        author = self.context.get('author',None)

        return Event.objects.create(author=author,**validated_data)


    def get_created_at(self,instance):
        return instance.created_at.isoformat()

    def get_image(self,obj):
        if obj.image:
            return obj.image
        return ''

    def get_updated_at(self,instance):
        return instance.updated_at.isoformat()


class CommentSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(read_only=True)

    text = serializers.CharField()

    created_at = serializers.SerializerMethodField(method_name="get_created_at")
    updated_at = serializers.SerializerMethodField(method_name="get_updated_at")

    class Meta:

        model = Comment

        fields = (
            'author',
            'text',
            'created_at',
            'updated_at'
        )  

    def create(self, validated_data):
        author = self.context['author']
        event = self.context['event']

        return Comment.objects.create(author=author,event=event,**validated_data)

    def get_updated_at(self,instance):
        return instance.updated_at.isoformat()

    def get_created_at(self,instance):
        return instance.created_at.isoformat()

    def get_favorited(self,instance):
        request = self.context.get('request',None)

        if request is None:
            return False
        
        if not request.is_authenticated():
            return False
        
        return request.user.profile.has_favorited(instance)