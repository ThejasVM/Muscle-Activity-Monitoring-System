from django.shortcuts import render

def live_graph(request):
    return render(request, 'myapp/index.html')
