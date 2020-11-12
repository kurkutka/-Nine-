from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        print(user_form.is_valid())
        if user_form.is_valid():
            print(1001)
            # Create a new user object but avoid saving it yet
            user_form.save()
            return redirect('/admin')
        else:
            print(1)
            user_form = UserCreationForm()
            return render(request, 'register.html', {'form': user_form})
    else:
        print(101)
        user_form = UserCreationForm()
        return render(request, 'register.html', {'form': user_form})
