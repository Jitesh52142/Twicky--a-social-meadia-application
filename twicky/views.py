from django.shortcuts import render, redirect, get_object_or_404
from .models import Twicky
from .forms import Twickyform,UserRegistrationsForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.

def index(request):
    return render(request, 'index.html')

# List all tweets
def Twickylist(request):
    tweets = Twicky.objects.all().order_by('-created_at')
    return render(request, 'twickylist.html', {'tweets': tweets})

# Create a new tweet
@login_required
def Twicky_create(request):
    if request.method == 'POST':
        form = Twickyform(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('Twickylist')
    else:
        form = Twickyform()

    return render(request, 'twicky_form.html', {'form': form})


# Edit an existing tweet
@login_required
def Twicky_edit(request, tweet_id):
    # Use filter().first() to avoid MultipleObjectsReturned error
    tweet = Twicky.objects.filter(pk=tweet_id, user=request.user).first()

    if not tweet:
        # Redirect to list page if tweet doesn't exist
        return redirect('Twickylist')

    if request.method == 'POST':
        form = Twickyform(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            return redirect('Twickylist')
    else:
        form = Twickyform(instance=tweet)

    return render(request, 'twicky_form.html', {'form': form})


# Delete a tweet
@login_required
def Twicky_delete(request, tweet_id):
    # Use filter().first() to prevent MultipleObjectsReturned
    tweet = Twicky.objects.filter(pk=tweet_id, user=request.user).first()

    if not tweet:
        # Redirect if tweet not found
        return redirect('Twickylist')

    if request.method == "POST":  # Fixed incorrect HTTP method check
        tweet.delete()
        return redirect('Twickylist')

    return render(request, 'twicky_delete.html', {'tweet': tweet})


def register(request):
    if request.method == "POST": # Fixed incorrect HTTP method check
        form = UserRegistrationsForm(request.POST) 
        if form.is_valid():
            user =form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            login(request, user)     
            return redirect('Twickylist') # Redirect to the home page after successful registration      
    else:
        form = UserRegistrationsForm()   
    return render(request, 'registration/register.html', {'form': form})
