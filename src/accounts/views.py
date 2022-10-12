from django.shortcuts import render
from accounts.models import User
# Create your views here.


def index(request):
    user = User.objects.get(username=admin)
    context = {'user':user}
    return render(request, 'index.html', context)
