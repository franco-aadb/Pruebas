#from django.shortcuts import render
#from django.http import JsonResponse
#from projectlist_app.models import Project
#
## Create your views here.
#def project_list(request):
#    project = Project.objects.all()
#    data = {
#        'projects' : list(project.values())
#    }
#    
#    return JsonResponse(data)
#
#def project_detail(request,key):
#    project = Project.objects.get(pk=key)
#    data = {
#        'name' : project.name,
#        'description' : project.decription,
#        'type' : project.type,
#        'status' : project.status,
#        'active' : project.active
#    }
#    
#    return JsonResponse(data)
