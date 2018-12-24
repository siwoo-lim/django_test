from django.shortcuts import render
from .models import CommentsData
from .forms import *
# Create your views here.

def comments_load(request):
    #comment = CommentsData.objects.order_by('-comments')
    comment = CommentsData.objects.all().order_by('-update_date')
    context = {'comment': comment}
    return render(request, 'comments/billboard.html', context)

def get_comment(request):
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Form()

    return render(request, 'comments/writecomment.html', {'form' : form })
