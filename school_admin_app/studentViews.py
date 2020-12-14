from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required(login_url='/login_page_show')
def student_home(request):
    context = {
        'page_title': "Student Dashboard"
    }

    return render(request, 'backend/pages/base/student_dashboard.html', context=context)
