from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import MyModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .form import CustomUserCreationForm
from django.contrib.auth import login
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.

@login_required
def home(request):
    # Get global task statistics (no user field)
    total_tasks = MyModel.objects.count()
    completed_tasks = MyModel.objects.filter(complete=True).count()
    pending_tasks = total_tasks - completed_tasks
    context = {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'user': request.user,
    }
    return render(request, "home.html", context)

@login_required
def todo(request):
    if request.method == "POST":
        # Handle adding new task
        task_title = request.POST.get('task_title')
        if task_title:
            MyModel.objects.create(title=task_title)
            messages.success(request, 'Task added successfully!')
            return redirect('todo')
    # Get all tasks (no user field)
    items = MyModel.objects.all()
    return render(request, "todos.html", {"items": items})

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(MyModel, id=task_id)
    task.complete = not task.complete
    task.save()
    messages.success(request, f'Task {"completed" if task.complete else "reopened"}!')
    return redirect('todo')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(MyModel, id=task_id)
    task.delete()
    messages.success(request, 'Task deleted successfully!')
    return redirect('todo')

def authView(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)  
            return redirect("home")
    else:
        form = CustomUserCreationForm()
        form.fields['username'].help_text = None
        form.fields['password1'].help_text = None
        form.fields['password2'].help_text = None

    return render(request, "registration/signup.html", {"form": form})


def username_recovery(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            send_mail(
                subject='Your Username Recovery',
                message=f'Hello,\n\nYour username is: {user.username}\n\nRegards,\nSupport Team',
                from_email='no-reply@example.com',
                recipient_list=[email],
            )
            return HttpResponse("If the email exists in our system, your username has been sent.")
        except User.DoesNotExist:
            return HttpResponse("If the email exists in our system, your username has been sent.")

    return render(request, 'username_recovery.html')

def profile_view(request):
    if request.method == 'POST':
        user = request.user
        username = request.POST.get('username')
        email = request.POST.get('email')

        if username and email:
            user.username = username
            user.email = email
            user.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
        else:
            messages.error(request, 'Please fill out all fields.')
    
    return render(request, 'profile.html', {'user': request.user})