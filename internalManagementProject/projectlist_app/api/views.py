from rest_framework import status, generics, mixins , viewsets, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle,ScopedRateThrottle
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from projectlist_app.models import Project,Category,Comment
from projectlist_app.api.serializers import ProjectSerializer,CategorySerializer,CommentSerializer
from projectlist_app.api.permissions import IsAdminOrReadOnly, IsCommentUserOrReadOnly
from projectlist_app.api.throttling import CommentCreateThrottle,CommentListThrottle
from projectlist_app.api.pagination import ProjectPagination,ProjectLOPagintion

# Create your views here.
# FILTROS
class CommentUser(generics.ListAPIView):
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        #llamada por url
        #username = self.kwargs['username']
        #llamada por parametro
        username = self.request.query_params.get('username', None)
        return Comment.objects.filter(comentario_user__username=username)
    
    
# METODOS CONCRETOS
class CommentList(generics.ListCreateAPIView):
    #queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    #permission_classes = [IsAuthenticated]
    throttle_classes = [CommentListThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['comentario_user__username','active']
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Comment.objects.filter(project=pk)
    
class CommentCreate(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [CommentCreateThrottle]
    def get_queryset(self):
        return Comment.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        projecto = Project.objects.get(pk=pk)
        user = self.request.user
        commentario_queryset = Comment.objects.filter(project = projecto,comentario_user=user)
        if commentario_queryset.exists():
            raise ValidationError("El usuario ya escribrió un comentario para este projecto")
        if projecto.number_rating == 0:
            projecto.avg_rating = serializer.validated_data['rating']
        else:
            projecto.avg_rating = (serializer.validated_data['rating'] + projecto.avg_rating)/2
        projecto.number_rating = projecto.number_rating + 1
        projecto.save()
        serializer.save(project=projecto,comentario_user=user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsCommentUserOrReadOnly]
    #throttle_classes = [UserRateThrottle,AnonRateThrottle]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'comentario-detail'
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

#VIEW SET
class CategoryVS(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
# class CategoryVS(viewsets.ViewSet):
#     def list(self,request):
#         queryset = Category.objects.all()
#         serializer = CategorySerializer(queryset,many = True)
#         return Response(serializer.data)
    
#     def retrieve(self,request,pk = None):
#         queryset = Category.object.all()
#         projectlist = get_object_or_404(queryset, pk=pk)
#         serializer = CategorySerializer(projectlist)
#         return Response(serializer.data)                    
        
#     def create(self,request):
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
#     def update(self,request,pk):
#         try:
#             categoria = Category.object.get(pk=pk)
#         except Category.DoesNotExist:
#             return Response({'Error':'Empresa no encontrada'},status=status.HTTP_404_NOT_FOUND)
#         serializer = CategorySerializer(categoria,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
#     def destroy(self,request,pk):
#         try:
#             categoria = Category.object.get(pk=pk)
#         except Category.DoesNotExist:
#             return Response({'Error':'Empresa no encontrada'},status=status.HTTP_404_NOT_FOUND)
#         categoria.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)
class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name','category__name'] #URL='/?name=&category__name='
    filter_backends = [filters.SearchFilter,filters.OrderingFilter] #order = &ordering=name
    search_fields = ['name','category__name']
    pagination_class = ProjectPagination
    #pagination_class = ProjectLOPagintion
        
class ProjectListAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
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
    permission_classes = [IsAdminOrReadOnly]
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
