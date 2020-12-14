import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from school_admin_app.EmailBackend import EBackEnd
from django.urls import reverse
from django.contrib import messages


# Create your views here.
def login_page_show(request):
    context = {
        'page_title': "School Management System Login"
    }
    return render(request, 'backend/pages/base/login.html', context=context)


def user_login(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EBackEnd.authenticate(request, username=request.POST.get("email"), password=request.POST.get("password"))
        if user is not None:
            login(request, user)
            if user.user_type == "1":
                return HttpResponseRedirect('/admin_dashboard')
            elif user.user_type == "2":
                return HttpResponseRedirect(reverse("staff_dashboard"))
            else:
                return HttpResponseRedirect(reverse("student_dashboard"))
        else:
            messages.error(request, "Invalid Login Details")
            return HttpResponseRedirect("/login_page_show")


@login_required(login_url='/login_page_show')
def get_user_details(request):
    if request.user is not None:
        return HttpResponse("User : " + request.user.email + " usertype : " + str(request.user.user_type))
    else:
        return HttpResponse("Please Login First")


def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/login_page_show")
