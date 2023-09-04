from rest_framework import serializers
from projectlist_app.models import Project,Category

class ProjectSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = Project
        exclude = ['id']
        
class CategorySerializer(serializers.ModelSerializer):
    #projectolist = ProjectSerializer(many=True, read_only=True)
    #projectolist = serializers.StringRelatedField(many=True)
    projectolist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #projectolist = serializers.HyperlinkedRelatedField(many=True, read_only=True,view_name='project-detail')
    class Meta:
        model = Category
        #fields = "__all__"
        exclude = ['id']