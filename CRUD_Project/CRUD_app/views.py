from django.shortcuts import (
    render,
    redirect,
    HttpResponseRedirect,
    reverse
)


from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .models import BlogModel
from .forms import BlogForm

# Create your views here.

def index(request):
    return render(request, 'CRUD_app/index.html')


class CreateBlog(SuccessMessageMixin, CreateView):
    model = BlogModel
    fields = ['title', 'description']

    success_message = 'Blog Created Successfully'

    success_url = reverse_lazy('blog_list')

    '''
    Generally, get_context_data will merge the context data of all 
    parent classes with those of the current class.
    '''
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Blog'
        return context



class BlogList(ListView):
    model = BlogModel



class BlogDetail(DetailView):
    model = BlogModel



class UpdateBlog(UpdateView):
    model = BlogModel
    fields = ['title', 'description']


    def get_success_url(self):
        pk = self.object.pk
        return reverse('blog_detail', kwargs={'pk': pk})

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Blog'
        return context



class DeleteBlog(DeleteView):
    model = BlogModel
    success_url = reverse_lazy('blog_list')

    '''def get_success_url(self):
        return reverse('blog_list')'''

