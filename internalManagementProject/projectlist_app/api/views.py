from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from projectlist_app.models import Project,Category
from projectlist_app.api.serializers import ProjectSerializer,CategorySerializer

# Create your views here.
class CategoryListAV(APIView):
    def get(self,request):
        categorias = Category.objects.all()
        serializer = CategorySerializer(categorias, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer2 = CategorySerializer(data = request.data)
        if serializer2.is_valid():
            serializer2.save()
            return Response(serializer2.data)
        else:
            return Response(serializer2.errors, status = status.HTTP_400_BAD_REQUEST)

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
