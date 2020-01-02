from django.shortcuts import render

# Create your views here.

def like(request):
    uid = request.GET.get('uid')
    wid = request.GET.get('wid')
    return render(....)
