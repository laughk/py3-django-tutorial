from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question {0}.".format(question_id))
