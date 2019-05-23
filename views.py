from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View

from .forms import CommentForm

from .models import Comment

# Create your views here.

class CommentCreate(View):
    def get(self, request):
        form = CommentForm()
        comments = Comment.objects.all()
        return render(request, 'chat/index.html', context={'comments':comments, 'form':form})

    def post(self, request):
        bound_form = CommentForm(request.POST)
        comments = Comment.objects.filter().order_by('date_pub')
        if bound_form.is_valid():
            new_comment = bound_form.save()
            return redirect(new_comment)
        return render(request, 'chat/index.html', context={'comments': comments, 'form': bound_form})