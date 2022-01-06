from django.shortcuts import redirect, render
from .models import Post
import os
from django.conf import settings
from django.core.paginator import Paginator

def index(request):
    return render(request, 'boardApps/index.html')

def list(request):
    page = request.GET.get('page', '1')
    postlist = Post.objects.all().order_by('-id')
    
    paginator = Paginator(postlist, 10)
    postlist = paginator.get_page(page)
    
    return render(request, 'boardApps/list.html', {'postlist':postlist})

def write(request):
    if request.method == 'POST':
        try:
            Post.objects.create (
                titles = request.POST['titles'],
                names = request.POST['names'],
                contents = request.POST['contents'],
                files = request.FILES['files'],
            )
        except:
            Post.objects.create (
                titles = request.POST['titles'],
                names = request.POST['names'],
                contents = request.POST['contents'],
            )
        return redirect('/boardApps/list/')
    return render(request, 'boardApps/write.html')

def view(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'boardApps/view.html', {'post':post})

def edit(request, pk):
    post = Post.objects.get(pk=pk)
    
    if request.method == 'POST':
        try:
            post.titles=request.POST['titles']
            post.names=request.POST['names']
            post.contents=request.POST['contents']
            post.files=request.FILES['files']
            
            os.remove(os.path.join(settings.MEDIA_ROOT, request.POST['prevfiles']))
        except:
            post.titles=request.POST['titles']
            post.names=request.POST['names']
            post.contents=request.POST['contents']
        post.save()
        return redirect('/boardApps/view/'+str(pk)+'/')
    else:
        return render(request, 'boardApps/edit.html', {'post':post})
    
def delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method=='GET':
        post.delete()
        return redirect('/boardApps/list/')