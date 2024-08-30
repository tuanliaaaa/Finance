from rest_framework.response import Response
from rest_framework import status

def RoleRequest(allowed_roles=[]):
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            user_role = getattr(request, 'Role', None)
            if user_role in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return Response({"message": "Bạn không có quyền truy cập"}, status=status.HTTP_403_FORBIDDEN)
        return wrap
    return decorator
