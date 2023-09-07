from django.urls import path,include
from rest_framework.routers import DefaultRouter
from projectlist_app.api.views import (ProjectListAV,ProjectDetailAV,CategoryListAV,CategoryDetailAV,CategoryVS,
CommentDetail,CommentList,CommentCreate)

router = DefaultRouter()
router.register('category',CategoryVS, basename='categoria')

urlpatterns = [
    #Project
    path('list/', ProjectListAV.as_view(), name='project-list'),
    path('<int:key>',ProjectDetailAV.as_view(), name='project-detail'),
    #Category
    path('',include(router.urls)),
    #path('category/', CategoryListAV.as_view(), name='category-list'),
    #path('category/<int:key>', CategoryDetailAV.as_view(), name='category-detail'), 
    #Comment
    path('<int:pk>/comment-create/', CommentCreate.as_view(), name='comment-create'),
    path('<int:pk>/comment/', CommentList.as_view(), name='comment-list'),
    path('comment/<int:pk>', CommentDetail.as_view(), name='comment-detail'), 
]
