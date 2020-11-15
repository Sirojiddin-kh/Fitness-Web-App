from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from . forms import UserNameForm, OnlineOfferForm, CreateUserForm
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from . models import Menu, FitnessExpert, SportProgramme, Gallary,Blog, Gratitude, UserName, ServiceCategory, Category
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic import FormView

@login_required(login_url='core:login')
def index(request):

    service = SportProgramme.objects.all()
    gratitude = Gratitude.objects.all()

    context = {

        'service': service,
        'gratitudes': gratitude}
    return render(request, 'index.html', context)





def gallery(request):
    menu = Menu.objects.all().order_by('order')
    images = Gallary.objects.all()

    context = {
        'menu': menu,
        'images': images}

    return render(request, 'gallery.html', context)


def trainer(request):
    menu = Menu.objects.all().order_by('order')
    expert = FitnessExpert.objects.all()
    context = {
        'menu': menu,
         "expert": expert}
    return render(request, 'about.html', context)


def pricing(request):
    menu = Menu.objects.all().order_by('order')
    services = ServiceCategory.objects.all()

    context = {
        'menu': menu,
        'services': services
        }
    return render(request, 'pricing.html', context)


def blog(request):
    menu = Menu.objects.all().order_by('order')
    categories = Category.objects.all()
    context = {
        'menu': menu,
        'categories': categories}
    return render(request, 'blog.html', context)


def detail(request, pk):
    menu = Menu.objects.all().order_by('order')
    details = Blog.objects.get(id=pk)
    print(pk)
    return render(request, 'detail.html', context={'menu': menu, 'object': details})



def contact(request):
    menu = Menu.objects.all().order_by('order')
    if request.method == 'POST':
        contact = UserName()
        name = request.POST.get('message_name')
        surname = request.POST.get('message_surname')
        subject = request.POST.get('message_subject')
        email = request.POST.get('message_email')
        message = request.POST.get('message')
        contact.name = name
        contact.surname = surname
        contact.subject = subject
        contact.email = email
        contact.request_message = message
        contact.save()
        return render(request, 'success.html')

    return render(request, 'contact.html', {'menu': menu})






"""class UserRequestForm(generic.FormView):
    form_class = UserNameForm
    template_name = 'contact.htm;'


    def form_valid(self, form):
        form.save()
        return super(UserRequestForm, self).form_valid(form)

    def get_success_url(self):
        return reverse('core:success')

def success(request):
    return render(request, "success.html")
"""




def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for " + user)
            return redirect('core:login')
    context = {'form': form}

    return render(request, 'register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('core:index')
        else:
            messages.info(request, "Username or pasaword is incorrect")

    return render(request, 'login.html', context={})


def logoutPage(request):
    logout(request)
    return redirect('login')


def search(request):
    searching = request.GET.get('blog')
    blog_list = Blog.objects.filter(title__icontains=searching)

    return render(request, 'search_result.html', {'list': blog_list})