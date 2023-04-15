from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import UserSerializer, UserRegisterSerializer
from django.shortcuts import render, redirect
from .grpc.grpc_client import create_text_content, create_user
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import IntroductionForm, ProfilePhotoForm, CoverPhotoForm


# Login view
def login(request):
    return render(request, 'login.html')

# User registration view using the DRF generic CreateAPIView
class UserRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    # Overriding the create method to use gRPC for user registration
    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        response = create_user(username, email, password)
        return JsonResponse({"status": "success", "user_id": response.user_id, "message": response.message})

# Homepage view
def homepage(request):
    return render(request, 'user_management/homepage.html')


# Profile view with introduction update functionality
@login_required
def profile_view(request, pk):
    user = CustomUser.objects.get(pk=pk)
    updated = False
    if request.method == "POST":
        form = IntroductionForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            updated = True
    else:
        form = IntroductionForm(instance=user)
    context = {'user': user, 'form': form, 'updated': updated}
    return render(request, 'user_management/profile.html', context)


# Introduction update view
@login_required
def update_introduction(request, pk):
    user = CustomUser.objects.get(pk=pk)
    if request.method == "POST":
        form = IntroductionForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_management:profile', pk=pk)
    else:
        form = IntroductionForm(instance=user)
    context = {'form': form}
    return render(request, 'user_management/update_introduction.html', context)

@login_required
def update_profile_photo(request, pk):
    user = CustomUser.objects.get(pk=pk)
    if request.method == "POST":
        form = ProfilePhotoForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_management:profile', pk=pk)
    else:
        form = ProfilePhotoForm(instance=user)
    context = {'form': form}
    return render(request, 'user_management/update_profile_photo.html', context)

@login_required
def update_cover_photo(request, pk):
    user = CustomUser.objects.get(pk=pk)
    if request.method == "POST":
        form = CoverPhotoForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_management:profile', pk=pk)
    else:
        form = CoverPhotoForm(instance=user)
    context = {'form': form}
    return render(request, 'user_management/update_cover_photo.html', context)
