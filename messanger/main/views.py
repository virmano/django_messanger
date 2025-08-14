from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import CommentsForm
from .models import Comments

# Create your views here.
def index(request):
    error = None

    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.created_at = timezone.now()

            if comment.reply:
                parent = Comments.objects.get(id=comment.reply.id)
                parent.has_reply = True
                parent.save()
            comment.save()

            return redirect("main")
        else:
            error = "CAPTCHA введена не верно!"
    else:
        form = CommentsForm()

    sort_param = request.GET.get('sort', '-created_at')
    comments = Comments.objects.filter(reply__isnull=True).order_by(sort_param)

    paginator = Paginator(comments, 25)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'main/index.html', {
        "comments": page_obj,
        'form': form,
        "error": error,
        "sort_param": sort_param
    })


def get_replies(request, comment_id):
    replies = Comments.objects.filter(reply_id=comment_id).order_by('created_at')
    return render(request, 'main/replies-list.html', {'replies': replies})