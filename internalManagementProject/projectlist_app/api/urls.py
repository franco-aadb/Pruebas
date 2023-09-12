from django.urls import path,include
from rest_framework.routers import DefaultRouter
from projectlist_app.api.views import (ProjectList,ProjectListAV,ProjectDetailAV,CategoryListAV,CategoryDetailAV,CategoryVS,
CommentDetail,CommentList,CommentCreate,CommentUser)

router = DefaultRouter()
router.register('category',CategoryVS, basename='categoria')

urlpatterns = [
    #Project
    path('list/', ProjectListAV.as_view(), name='project-list'),
    path('<int:key>',ProjectDetailAV.as_view(), name='project-detail'),
    path('filter/',ProjectList.as_view(), name='project-filter'),
    #Category
    path('',include(router.urls)),
    #path('category/', CategoryListAV.as_view(), name='category-list'),
    #path('category/<int:key>', CategoryDetailAV.as_view(), name='category-detail'), 
    #Comment
    path('<int:pk>/comment-create/', CommentCreate.as_view(), name='comment-create'),
    path('<int:pk>/comment/', CommentList.as_view(), name='comment-list'),
    path('comment/<int:pk>', CommentDetail.as_view(), name='comment-detail'), 
    #path('comment/<str:username>', CommentUser.as_view(), name='comment-user'), 
    path('comment/', CommentUser.as_view(), name='comment-user'), 
]
