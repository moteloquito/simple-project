from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import CustomUser


@login_required
def landscape(request):
    u = CustomUser.objects.get(user=request.user)
    return render(request, 'users/landscape.html', {'user': u})
