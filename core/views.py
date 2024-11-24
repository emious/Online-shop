
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        # کاربر وارد شده است
        return render(request, 'core/index-14.html')
    else:
        return HttpResponse('karbar nis')