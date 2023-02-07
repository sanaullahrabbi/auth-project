from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from app_auth.serializers import UserSerializer
from app_auth.models import User


class UserListCreateView(ListCreateAPIView):
    permission_classes = []
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetriveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = UserSerializer
    queryset = User.objects.all()

