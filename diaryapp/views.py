from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Event
from .forms import RegistrationForm, MemoryUpdate
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# class EventListView(LoginRequiredMixin, ListView):
#     model = Event
#     template_name = "diaryapp/home.html"
#     context_object_name = 'events'

#     def get_queryset(self):
#         return Event.objects.filter(author=self.request.user).order_by('-date_posted')

def home(request):
    return render(request, 'diaryapp/home.html')


@login_required
def memories(request):
    events = Event.objects.filter(author=request.user).order_by('-date_posted')

    context = {'events': events}
    return render(request, 'diaryapp/memories.html', context)


def detail(request, memory_pk):
    mem = get_object_or_404(Event, pk=memory_pk)
    context = {'event': mem}
    return render(request, 'diaryapp/detail.html', context)


def delete(request, memory_pk):
    get_object_or_404(Event, pk=memory_pk).delete()

    return redirect('memories')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'diaryapp/register.html', context)


def UpdateMem(request, memory_pk):
    mem = Event.objects.get(id=memory_pk)
    if request.method == 'POST':
        form = MemoryUpdate(request.POST, instance=mem)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('detail', memory_pk)
    else:

        form = MemoryUpdate(instance=mem)
        context = {'form': form}
        return render(request, 'diaryapp/update.html', context)


def NewMem(request):
    if request.method == 'POST':
        form = MemoryUpdate(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            pdd = Event.objects.last()
            return redirect('detail', pdd.id)
    else:
        form = MemoryUpdate()
        context = {'form': form}
        return render(request, 'diaryapp/update.html', context)

# class UpdateMem(LoginRequiredMixin, UpdateView):
#     model = Event
#     template_name = 'diaryapp/update.html'


# class NewMem(LoginRequiredMixin, CreateView):
#     model = Event
#     template_name = 'diaryapp/update.html'
#     fields = ['title', 'content']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
