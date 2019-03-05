from django.shortcuts import redirect,render,HttpResponseRedirect,HttpResponse,redirect
from .models import *
from django.shortcuts import get_object_or_404, Http404
from .forms import PostForm,ContactForm
from django.contrib import messages

from django.core.paginator import Paginator

def post_detail(request, id, slug):
    instance=get_object_or_404(Post,id=id)

    c = {'title': instance.title,
         'instance': instance}

    return render(request, 'detail.html',c)




def post_create(request):
    if not request.user.is_staff: #or not request.user.is_superuser:
        raise Http404
    form=PostForm(request.POST, request.FILES )
    if request.method=='POST':
        obj=form.save(commit=False)
        obj.save()
      #  obj.user=request.user
        messages.success(request,'successfully created your post')
        return HttpResponseRedirect(obj.get_absolute_url())

    c = {'form':form, 'title':'create'}
    return render(request, 'form.html',c)





def post_list(request):
    query_list = Post.objects.all().order_by("-timestamp")

    qry=request.GET.get('q')
    if qry:
        query_list=query_list.filter(title__icontains=qry)

    paginator = Paginator(query_list, 5)  # Show 25 contacts per page
    page = request.GET.get('page')
    query = paginator.get_page(page)
    c = { 'object':query, 'title':'Blogs'}
    return render(request, 'list.html',c)



def post_update(request,id,slug):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    instance = get_object_or_404(Post, id=id,slug=slug)

    form = PostForm(request.POST, request.FILES , instance=instance)
    if request.method == 'POST':
        obj = form.save(commit=False)
        obj.save()
        messages.success(request,'successfully updated')
        return HttpResponseRedirect(instance.get_absolute_url())

    c = {'title': instance.title,
         'instance': instance, 'form':form}


    return render(request, 'u_form.html',c)

def post_delete(request,id,slug):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance=get_object_or_404(Post,id=id,slug=slug)
    instance.delete()
    messages.success(request, 'post successfully deleted')
    return redirect('posts:list')




def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():

            cf=form.save(commit=False)
            cf.save()

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            comments = form.cleaned_data['comments']
           # messages.success(request,'Got your Info back to you soon ')
            return HttpResponseRedirect('/posts/contactus/completed')
    else:
        form=ContactForm()
    return render(request,'contact.html',{'form':form})

def completed(request):
    return render(request,'completed.html')

def readme(request):
    #data=open('C:/Users/Shubh/Desktop/DjangoApi/static/readme.txt','r')
    #data_content=data.read()
    #data.close()
    return render(request,'readme.txt')

