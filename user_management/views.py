from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import logout
from rest_framework import status
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet
from .forms import IntroductionForm

# UserViewSet
class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    # Overriding the get_permissions method to allow unauthenticated users to register
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]


# Logout View
class LogoutView(APIView):
    def get(self, request, format=None):
        logout(request)
        return Response(status=status.HTTP_200_OK)


# Profile view with introduction update functionality
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        user = CustomUser.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        user = CustomUser.objects.get(pk=pk)
        form = IntroductionForm(request.data, instance=user)
        if form.is_valid():
            form.save()
            serializer = UserSerializer(user)
            return Response(serializer.data)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


# Introduction update view
class UpdateIntroductionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, format=None):
        user = CustomUser.objects.get(pk=pk)
        form = IntroductionForm(request.data, instance=user)
        if form.is_valid():
            form.save()
            serializer = UserSerializer(user)
            return Response(serializer.data)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
