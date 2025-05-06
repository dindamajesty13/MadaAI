from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from myapp.serializers import UserSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_data(request):
    """Returns the authenticated user's data"""
    user = request.user  # Get the currently logged-in user
    serializer = UserSerializer(user)
    return Response(serializer.data)