from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class ProjectPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'p' #se cambia de ?page a ?p
    page_size_query_param = 'size'
    max_page_size_size = 10
    
class ProjectLOPagintion(LimitOffsetPagination):
    default_limit = 1
    