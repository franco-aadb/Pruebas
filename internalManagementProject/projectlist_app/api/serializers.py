from rest_framework import serializers
from projectlist_app.models import Project,Category,Comment

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        #fields = "__all__"
        exclude = ['project']

class ProjectSerializer(serializers.ModelSerializer): 
    comentarios = CommentSerializer(many=True,read_only=True)
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
        