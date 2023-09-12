from rest_framework import serializers
from projectlist_app.models import Project,Category,Comment

class CommentSerializer(serializers.ModelSerializer):
    comentario_user = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Comment
        #fields = "__all__"
        exclude = ['project']

class ProjectSerializer(serializers.ModelSerializer): 
    comentarios = CommentSerializer(many=True,read_only=True)
    category_name = serializers.CharField(source='category.name')
    class Meta:
        model = Project
        fields = "__all__"
        
class CategorySerializer(serializers.ModelSerializer):
    projectolist = ProjectSerializer(many=True, read_only=True)
    #projectolist = serializers.StringRelatedField(many=True)
    #projectolist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #projectolist = serializers.HyperlinkedRelatedField(many=True, read_only=True,view_name='project-detail')
    class Meta:
        model = Category
        fields = "__all__"
        #exclude = ['id']
        