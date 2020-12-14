from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required(login_url='/login_page_show')
def staff_dashboard(request):
    context = {
        'page_title': "Staff Dashboard"
    }

    return render(request, 'backend/pages/base/staff_dashboard.html', context=context)

