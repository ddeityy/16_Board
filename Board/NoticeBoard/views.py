from django.shortcuts import HttpResponseRedirect, redirect
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *


class Board(ListView):
    model = BoardNotice
    ordering = '-creation'
    template_name = 'board.html'
    context_object_name = 'board'
    paginate_by = 5
    
    def get_queryset(self):
        return super().get_queryset()

class MyResponses(ListView):
    model = Response
    ordering = '-creation'
    template_name = 'my_responses.html'
    context_object_name = 'responses'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = BoardNotice.objects.filter(user_id=self.request.user.id)\
            .values_list('user_id', flat=True)
        return context

@login_required
def accept(self, pk):
    Response.objects.filter(id=pk).update(accepted=True)
    return redirect('/accounts/profile/')

class DeleteResponce(LoginRequiredMixin, DeleteView):
    model = Response
    template_name = 'delete.html'
    success_url = reverse_lazy('board')

class NoticeDetail(LoginRequiredMixin, DetailView):
    model = BoardNotice
    template_name = 'notice.html'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['responses'] = Response.objects.filter(response_to_id=self.kwargs.get('pk'))
        return context

class RespondToPost(LoginRequiredMixin, CreateView):
    model = Response
    form = ResponseForm
    fields = ['text',]
    template_name = 'respond.html'
    success_url = "/board/post/{}"
    context_object_name = 'response'
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.response_user = self.request.user
        self.object.response_to_id = self.kwargs.get('pk')
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self, **kwargs):
        return reverse('notice_detail', kwargs={'pk': self.kwargs.get('pk')})

class DeletePost(LoginRequiredMixin, DeleteView):
    model = BoardNotice
    template_name = 'delete.html'
    success_url = reverse_lazy('board')

class CreateNotice(LoginRequiredMixin, CreateView):
    form_class = BoardForm
    model = BoardNotice
    template_name = 'notice_edit.html'
    context_object_name = 'board_new'
    success_url = reverse_lazy('board')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class EditNotice(LoginRequiredMixin, UpdateView):
    form_class = BoardForm
    model = BoardNotice
    template_name = 'notice_edit.html'
    context_object_name = 'board_new'
    success_url = reverse_lazy('board')
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())