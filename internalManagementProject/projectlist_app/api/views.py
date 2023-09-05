from rest_framework import status, generics, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from projectlist_app.models import Project,Category,Comment
from projectlist_app.api.serializers import ProjectSerializer,CategorySerializer,CommentSerializer

# Create your views here.
# METODOS CONCRETOS
class CommentList(generics.ListCreateAPIView):
    #queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Comment.objects.filter(project=pk)
    
class CommentCreate(generics.CreateAPIView):
    serializer_class = CommentSerializer
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        projecto = Project.objects.get(pk=pk)
        serializer.save(project=projecto)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
# METODOS GENERICOS
# class CommentList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
    
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args, **kwargs)
    
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args, **kwargs)
    
# class CommentDetail(mixins.RetrieveModelMixin,generics.GenericAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
    
#     def get(self,request,*args, **kwargs):
#         return self.retrieve(request,*args,**kwargs)

class CategoryListAV(APIView):
    def get(self,request):
        categorias = Category.objects.all()
        serializer = CategorySerializer(categorias, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CategoryDetailAV(APIView):
    def get(self,request,key):
        try:
            categoria = Category.objects.get(pk=key)
        except Category.DoesNotExist:
            return Response({'error':'Categoria no encontrada'},status = status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(categoria,context = {'request':request})
        return Response(serializer.data)
    
    def put(self,request,key):
        try:
            categoria = Category.objects.get(pk=key)
        except Category.DoesNotExist:
            return Response({'error':'Categoria no encontrada'},status = status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(categoria,data = request.data,context = {'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,key):
        try:
            categoria = Category.objects.get(pk=key)
        except Category.DoesNotExist:
            return Response({'error':'Categoria no encontrada'},status = status.HTTP_404_NOT_FOUND)
        categoria.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        
class ProjectListAV(APIView):
    def get(self,request):
        projectos = Project.objects.all()
        serializer = ProjectSerializer(projectos,many = True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ProjectSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

class ProjectDetailAV(APIView):
    def get(self,request,key):
        try:
            projecto = Project.objects.get(pk = key)
        except Project.DoesNotExist:
            return Response({'Error:','Projecto no encontrado'},status = status.HTTP_404_NOT_FOUND)
        serializer = ProjectSerializer(projecto)
        return Response(serializer.data)
    
    def put(self,request,key):
        try:
            projecto = Project.objects.get(pk = key)
        except Project.DoesNotExist:
            return Response({'Error:','Projecto no encontrado'},status = status.HTTP_404_NOT_FOUND)
        serializer = ProjectSerializer(projecto,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,key):
        try:
            projecto = Project.objects.get(pk = key)
        except Project.DoesNotExist:
            return Response({'Error:','Projecto no encontrado'},status = status.HTTP_404_NOT_FOUND)
        serializer = ProjectSerializer(projecto)
        projecto.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
