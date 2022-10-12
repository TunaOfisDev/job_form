
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm
from accounts.forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import CustomUser
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from django import forms
from .forms import PostForm
from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    # template_name = 'post_list.html'

  
class PostDetail(generic.DetailView):
    queryset = Post.objects.all().order_by("-created_on")
    # template_name = 'post_detail.html'


class CreatePost(LoginRequiredMixin, generic.CreateView):
    login_url = reverse_lazy("login")
    success_url = reverse_lazy("post_list")

    form_class = PostForm
    # model = Post
    queryset = Post.objects.all()
    template_name = "blog/post_form.html"

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        request.POST._mutable = True
        request.POST["author"] = request.user
        request.POST._mutable = False

        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy("login")
    # success_url = reverse_lazy("post_detail", kwargs={'pk': post.id})

    # model = Post
    # template_name = 'blog/post_form.html'
    queryset = Post.objects.all()
    form_class = PostForm

    def get_success_url(self, **kwargs):
        return reverse_lazy(
            "post_detail",
            args=(
                {
                    self.object.id,
                }
            ),
        )


class PostDelete(LoginRequiredMixin, generic.DeleteView):
    queryset = Post.objects.all().order_by("-created_on")  # .filter(status=1)
    success_url = reverse_lazy("post_list")


class PostDraftList(LoginRequiredMixin, generic.ListView):
    login_url = reverse_lazy("login")
    queryset = Post.objects.filter(status=0).order_by("-created_on")

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)


class PostArchivedList(LoginRequiredMixin, generic.ListView):
    login_url = reverse_lazy("login")
    queryset = Post.objects.filter(status=2).order_by("-created_on")

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)


@login_required
def post_publish(request, pk):
    Post.objects.filter(pk=pk).update(status=1)
    return redirect("post_detail", pk=pk)


@login_required
def post_archive(request, pk):
    Post.objects.filter(pk=pk).update(status=2)
    return redirect("post_detail", pk=pk)




class CreateUser(generic.CreateView):
    success_url = reverse_lazy("post_list")

    form_class = CustomUserCreationForm
    queryset = CustomUser.objects.all()
    template_name = "registration/signup.html"

class Meta(forms.ModelForm):
    model = CustomUser
    fields = '__all__'