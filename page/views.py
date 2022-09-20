from django.shortcuts import render

# Create your views here.


# vista del la pagina de inicio
def home_page(request):
    return render(request, 'page/home_page.html')


# Vista de acerca del proyecto
def about_page(request):
    return render(request, 'page/about.html')
