from rest_framework.throttling import UserRateThrottle

class CommentCreateThrottle(UserRateThrottle):
    scope = 'comentario-create'
    
class CommentListThrottle(UserRateThrottle):
    scope = 'comentario-list'