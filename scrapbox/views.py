from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.views.generic import View,CreateView,FormView,UpdateView,ListView
from scrapbox.forms import RegisterationForm,LoginForm,ScrapForm,ProfileForm
from django.urls import reverse
from django.contrib import messages
from scrapbox.models import Userprofile,Scraps

# Create your views here.

class SignUpView(CreateView):

    template_name="register.html"
    form_class=RegisterationForm


    def get_success_url(self):
        return reverse("signin")
    
class SignInView(FormView):
   template_name="login.html"
   form_class=LoginForm

   def post(self, request,*args, **kwargs):
       form=LoginForm(request.POST)
       if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_obj=authenticate(request,username=uname,password=pwd)
            if user_obj:
                login(request,user_obj)
                print(request.user)
                return redirect("index")
            print(request.user)
       return render(request,"login.html",{"form":form})
    
class IndexView(ListView):

    template_name="index.html"
    context_object_name="data"
    model=Scraps
    
    def get_queryset(self):
        qs=Scraps.objects.all()
        return qs    


class ScrapAddView(CreateView):
    template_name="scrapadd.html"
    form_class=ScrapForm
    
    def form_valid(self, form: BaseModelForm):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("index")
    


class UserProfileView(UpdateView):
    template_name="profile.html"
    form_class=ProfileForm
    model=Userprofile

    def get_success_url(self):
        return reverse("index")

class ProfileDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Userprofile.objects.get(id=id)
        return render(request,"profiledetail.html",{"data":qs})


class ScrapDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Scraps.objects.get(id=id)
        return render(request,"scrapdetail.html",{"data":qs})
    
class ScrapUpdateView(UpdateView):
    template_name="scrapedit.html"
    form_class=ScrapForm
    model=Scraps

    def get_success_url(self):
        return reverse("index")


class ScrapDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Scraps.objects.get(id=id).delete()
        return redirect("index")

class SignOutView(View):

    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")
    
