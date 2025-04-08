from django.shortcuts import render

# Create your views here.
def ReturnMain(request):
    return render(request, 'general_main.html')