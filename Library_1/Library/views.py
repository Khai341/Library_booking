from django.shortcuts import render


def homepage(request):
    if request.user.is_authenticated and hasattr(request.user, 'status'):
        if request.user.status == 'G':
            return render(request, 'general_main.html')
        else:
            return render(request, 'official_main.html')
    return render(request, 'layout.html')