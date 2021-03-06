from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from articleapp.models import Article

has_ownership = [account_ownership_required, login_required]



class AccountCreateView(CreateView):
    model = User #상속
    form_class = UserCreationForm #장고가 기본제공
    #success_url = reverse_lazy('accountapp:detail')
    template_name = 'accountapp/create.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.pk})

class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)

@method_decorator (has_ownership, 'get')
@method_decorator (has_ownership, 'post')

class AccountUpdateView(UpdateView):
    model = User  # 상속
    context_object_name = 'target_user'
    form_class = AccountUpdateForm  # 장고가 기본제공
    #success_url = reverse_lazy('accountapp:detail')
    template_name = 'accountapp/update.html'
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.pk})

@method_decorator (has_ownership, 'get')
@method_decorator (has_ownership, 'post')

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'



    #함수와 클래스의 불러오는 방식이 달라서, reverse를 그대로 사용할 수 없다.
    #reverse_lazy는 클래스 뷰에서 사용하고 reverse는 함수 뷰에서 사용한다.