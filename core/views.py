from django.http import HttpResponse

def home(request):
    return HttpResponse("Инспекторская группа, здесь главное меню")