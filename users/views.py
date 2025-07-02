from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import EmailAuthenticationForm,CustomUserCreationForm
from .forms import Profile,ProfileForm

@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'users/dashboard.html')  

def register_view(request):
    if request.method == 'POST':  
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('dashboard')  
        else:
            messages.error(request, 'Error creating account. Please correct the errors below.') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "Login successful! Welcome back. 😊")
            return redirect('dashboard')
        else:
             messages.error(request, "Invalid email or password. Please try again.")
    else:
        form= EmailAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def start_scan(request):
    return render(request, 'users/start_scan.html') 

@login_required
def user_account(request):
    return render(request, 'users/user_account.html', {'user': request.user}) 

@login_required
def start_scan(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']

        # TODO: Replace this mock result with your ML/Scan logic
        result = "Scan complete! No issues found."

        return render(request, 'users/dashboard.html', {
            'result': result,
        })

    return redirect('dashboard')

@login_required
def user_account(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('user_account')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'users/user_account.html', {'form': form, 'profile': profile})