from django.shortcuts import render, get_object_or_404, redirect  #For FBV comments
from django.utils import timezone   #For FBV comments & ListView
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required  #--->For login purpouse --->FBV
from django.urls import reverse_lazy
from .models import Post

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'home.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    #context_object_name = 'anything_you_want' #we can name anything, DetailView gives individual object so we dont need to iterate. and we call it object as post or we can set the name for them like context_object_name = 'any_name'.But we have to use the object name correctly at the time of clling in template.

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name ='post_new.html'
    fields = ['author','title','body','image']   # we want required fields in model to show in our page like we create a post in admin site.
    #or we can create a form using post model,the mention it like below insted of writing fields in classes.
    #form_calss = PostForm
class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body'] # Again we can also ention required field to show in our page.

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    #We use reverse_lazy as opposed to just reverse so that it won’t execute the URL
    #redirect until our view has finished deleting the blog post.

class AboutView(TemplateView):
    template_name = 'about.html'

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()   #This method came from Post model
    return redirect('post_detail',pk=pk)




#Note:
# Login and logout are part of Django and rely on internal views and url routes.
