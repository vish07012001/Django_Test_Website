from django.http import HttpResponse

def about_us(request):
    return HttpResponse("About us page")