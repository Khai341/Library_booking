from django.shortcuts import render

# Create your views here.
def ReturnMain(request):
    return render(request, 'librarianAdmin_main.html')