from django.shortcuts import render, redirect

# Create your views here.

from django.shortcuts import (
    render, redirect, get_object_or_404
)
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView
)
from django.views.generic import (
    CreateView, UpdateView, TemplateView, ListView, DeleteView, DetailView
)
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import (
    LoginForm, ProfileForm, SignUpForm, PasswordForm
)
from .models import (
    User,
)

from django.contrib.auth.mixins import UserPassesTestMixin


class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True     # set True if raise 403_Forbidden

    def test_func(self):
        user = self.request.user
        if not user.is_authentiated:
            return False
        return user.pk == self.kwargs['pk'] or user.is_superuser



# Create your views here.
class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'main/login.html'

class Top(LoginRequiredMixin, TemplateView):
    template_name = 'main/top.html'

    def get(self, request):
        return redirect('main:profile', request.user.pk)

class Logout(LogoutView):
    pass

    
class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = reverse_lazy('main:login')
    template_name = 'main/signup.html'
    
    def form_valid(self, form):
        ret = super().form_valid(form)
        messages.success(self.request, f'ユーザ:{self.object.username} 登録完了しました。')
        return ret

from .models import category1s, category2s
class ListCompany(ListView):
    model = User
    template_name = 'main/list_company.html'
    paginate_by = 3
    
    def get_context_data(self, **kwargs):
        total_count = self.get_queryset().count()
        c = super().get_context_data(**kwargs)
        c['total_count'] = total_count
        c['category1s'] = category1s
        c['category2s'] = category2s
        c1 = self.request.GET.getlist('category1s')
        c2 = self.request.GET.getlist('category2s')
        c['query_params'] = { 
            'category1s': c1,
            'category2s': c2,
            'query': self.request.GET.get('query', '')
        }
        print(c['total_count'])
        return c

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-pk')
        c1 = self.request.GET.getlist('category1s')
        c2 = self.request.GET.getlist('category2s')
        query = self.request.GET.get('query', None)
        if len(c1) > 0:
            queryset = queryset.filter(category1__in = c1)
        if len(c2) > 0:
            queryset = queryset.filter(category2__in = c2)
        if query:
            queryset = queryset.filter(company_name__icontains = query)
        return queryset

class DetailCompany(DetailView):
    model = User
    template_name = 'main/detail_company.html'
    
class Profile(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm   
    template_name = 'main/profile.html'
    def get_success_url(self):
        return reverse_lazy('main:profile', kwargs={ "pk": self.kwargs["pk"] })
    
    def form_valid(self, form):
        messages.success(self.request, '登録情報を更新しました')
        return super().form_valid(form)
