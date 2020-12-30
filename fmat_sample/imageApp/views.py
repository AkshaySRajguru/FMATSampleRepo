from django.shortcuts import render
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
# Mongo Connection
from pymongo import MongoClient

# Create your views here.

cluster = MongoClient("mongodb://127.0.0.1:27017/fmatdb")
db = cluster["fmatdb"]
collection = db["fmatdbconnection"]


# Create your views here.
class WelcomeView(TemplateView):
    template_name = 'imageApp/welcome.html'


class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'imageApp/post_list.html'
    form_class = PostForm
    model = Post
    initial = {'key': 'value'}

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         # <process form cleaned data>
    #         collection.insert({"title": form.cleaned_data['title'], "text": form.cleaned_data['text']})
    #         for x in collection.find({"title": "Tire Basics"}):
    #             print(x)
    #
    #         # return HttpResponseRedirect('/success/')
    #         print('\n***********Hello World\n*******')
    #
    #     return render(request, self.redirect_field_name, {'form': form})


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.all()


class PostDetailView(DetailView):
    model = Post

# def form_name_view(request):
#     form = forms.FormName()
#
#     if request.method == 'POST':
#         form = forms.FormName(request.POST)
#
#
#         if form.is_valid():
#             print("Validation Success")
#             collection.insert({"name":form.cleaned_data['name'],"text": form.cleaned_data['text']})
#             print("Name: "+form.cleaned_data['name'])
#             print("Email: "+form.cleaned_data['email'])
#             print("Text: "+form.cleaned_data['text'])
#             form = forms.FormName()
#
#
#     return render(request,'form_page.html',{'form':form})
