from django.shortcuts import render
from django.urls import reverse_lazy
from movie1.models import Movie
from movie1.forms import movieform
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.
# def home(request):
#     b=Movie.objects.all()
#     return render(request,'home.html',{'b':b})

class MovieList(ListView):
    model = Movie
    template_name = "home.html"
    context_object_name = "b"

# def addmovie(request):
#     if(request.method=="POST"):
#         n=request.POST['n']
#         d=request.POST['d']
#         i=request.FILES['i']
#         b=Movie.objects.create(name=n,description=d,image=i)
#         b.save()
#         return MovieList(request)
#     return render(request,'addmovie.html')

class MovieAdd(CreateView):
    model = Movie
    template_name = "addmovie.html"
    fields='__all__'
    success_url=reverse_lazy('movie1:home')

# def movie_detail(request,p):
#     k = Movie.objects.get(id=p)
#     return render(request, 'movie_detail.html',{'k':k})

class MovieDetail(DetailView):
    model = Movie
    template_name = "movie_detail.html"
    context_object_name = "k"

# def update(request,p):
#     b=Movie.objects.get(id=p)
#     if (request.method == "POST"): #after submission
#         form = movieform(request.POST,request.FILES,instance=b)
#         if form.is_valid():
#             form.save()
#             return MovieList(request)
#     form=movieform(instance=b)
#     return render(request,'update.html',{'form':form})
class MovieUpdate(UpdateView):
    model = Movie
    template_name = "addmovie.html"
    fields='__all__'
    success_url=reverse_lazy('movie1:home')

# def delete(request,p):
#     b = Movie.objects.get(id=p)
#     b.delete()
#     return MovieList(request)

class MovieDelete(DeleteView):
    model = Movie
    # fields='__all__'
    success_url = reverse_lazy('movie1:home')
    template_name = "delete.html"
