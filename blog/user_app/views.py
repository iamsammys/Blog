from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .forms import UserRegistrationForm
from django.urls import reverse
from django.contrib.auth import views as auth_views
from .forms import UserUpdateForm, ProfileUpdateForm


def register(request):
    """Register user
    
    Attributes:
        request: request object
    
    Returns:
        render: render object
    """
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created for {}!\n Kindly login to continue!".format(form.cleaned_data["username"]))
            return redirect("login")
    else:
        form = UserRegistrationForm()
    return render(request, "user_app/register.html", {"form": form})

def profile(request):
    """Return profile page
    
    Attributes:
        request: request object
    
    
    Returns:
        render: render object
    """
    if not request.user.is_authenticated:
        messages.warning(request, "You need to login to view this page!")
        return redirect("{}?next={}".format(reverse("login"), request.path))
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully!")
        return redirect("profile")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)

    context = {
        "user_form": user_form,
        "profile_form": profile_form
    }
    return render(request, "user_app/profile.html", context)

def logout(request):
    """Logout user
    
    Attributes:
        request: request object
    
    Returns:
        redirect: redirect object
    """
    if not request.user.is_authenticated:
        messages.warning(request, "You need to login first!")
        return redirect("{}?next={}".format(reverse("login"), request.path))
    messages.info(request, "Logged out successfully!")
    return auth_views.LogoutView.as_view(template_name="user_app/logout.html")(request)
