from django.shortcuts import render
from movieapp.models import Movie
from movieapp.forms import movieforms


# Create your views here.
def addhome(request):
    srk = Movie.objects.all()
    return render(request, 'homepage.html', {"srk": srk})


def detail(request, n):
    m = Movie.objects.get(id = n)
    return render(request, 'detail.html', {'m': m})


def addmovie(request):
    if (request.method == 'POST'):
        frm = movieforms(request.POST, request.FILES)
        if frm.is_valid():
            frm.save()
            return addhome(request)
    form = movieforms()
    return render(request, 'add.html', {'form': form})
def deletemovie(request,dl):
    l=Movie.objects.get(id=dl)
    l.delete()
    return addhome(request)
def updatemovie(request,mv):
    l=Movie.objects.get(id=mv)
    form = movieforms(instance=l)
    if (request.method == 'POST'):
        frm = movieforms(request.POST, request.FILES,instance=l)
        if frm.is_valid():
            frm.save()
            return addhome(request)
    return render(request, 'update.html', {'form': form})



