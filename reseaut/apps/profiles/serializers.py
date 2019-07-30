from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    last_name = serializers.CharField(source='user.last_name')
    bio = serializers.CharField(allow_blank=True,required=False)
    #work_domain = serializers.CharField(max_length=50)
    image = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ('last_name','bio','image')#,'work_domain')
        read_only_fields = ('last_name',)

    def get_image(self,obj):
        if obj.image:
            return obj.image
        return 'https://image.flaticon.com/icons/svg/1738/1738691.svg'
    
    def get_following(self,instance):

        request = self.context.get('request',None)

        if request is None:
            return False
        
        if not request.user.is_authenticated:
            return False
        
        follower = request.user.profile
        followee = instance

        return follower.is_following(followee)