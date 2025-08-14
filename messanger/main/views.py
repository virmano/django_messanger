from django.shortcuts import render
from .models import Comments

# Create your views here.
def index(request):
    comments = Comments.objects.filter(reply__isnull=True).order_by('-created_at')


    return render(request, 'main/index.html',{
        "comments": comments
    })