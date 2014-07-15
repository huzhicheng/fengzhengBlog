#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import Http404
from django.http import HttpResponse
from fengzhengBlog.blogapp.models import fz_user
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
from fengzhengBlog.blogapp.views import home
import logging
import simplejson


# Create your views here.


def check_auth_redirect(request,template_name):
    #raise Http404(template_name,request,request.user.username,'hello',attrs)
    if request.user.is_authenticated():
       return render_to_response(template_name,{"currentUser":request.user.first_name+request.user.last_name})
    else:
        #raise Http404()
        return render_to_response("fengzhengadmin/login.html")
       #return render_to_response("fengzhengadmin/index.html")

@csrf_exempt
def checkuser(request):
    if request.method == "POST":
        username =request.POST.get("Username")
        password = request.POST.get("Password")
        log = logging.getLogger("customapp.engine")
        log.error("%s:%s",username,password)
        user=authenticate(username=username,password=password)  #huzhicheng Zhicheng.hu
    if user is not None:
         login(request, user)
         return HttpResponse('{"success":"ok"}')
    else:
        return HttpResponse('{"success":"fail"}')



def console(request):
    return render_to_response("fengzhengadmin/index.html",{"currentUser":request.user})

def fengzhenglogout(request):
    logout(request)
    if not request.user.is_authenticated():
        return home(request)