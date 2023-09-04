from django.urls import path
from projectlist_app.api.views import ProjectListAV,ProjectDetailAV,CategoryListAV,CategoryDetailAV

urlpatterns = [
    #Project
    path('list/', ProjectListAV.as_view(), name='project-list'),
    path('<int:key>',ProjectDetailAV.as_view(), name='project-detail'),
    #Category
    path('category/', CategoryListAV.as_view(), name='category-list'),
    path('category/<int:key>', CategoryDetailAV.as_view(), name='category-detail'),
]
