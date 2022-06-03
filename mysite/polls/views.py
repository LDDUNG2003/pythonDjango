from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    myname ="Lê Đình Dũng"
    taisan = ["Máy tính", "Điện thoại", "Máy ảnh"]
    return render(request, "polls/index.html",{'name':myname,'items':taisan})

def viewsQuestion(request):
    list_question = Question.objects.all()
    context = {"dsquest": list_question}
    return render(request, "polls/list.html", context)
def detalViews(request, question_id):
    q =Question.objects.get(pk=question_id)
    return render(request, "polls/veiwsQuestion.html", {"qs": q}) 
def vote(request, question_id):
    q = Question.objects.get(pk=question_id)
    try:
        data = request.POST['choice']
        c = q.choice_set.get(pk=data)
    except:
        HttpResponse("error no objects")
    c.vote = c.vote + 1
    c.save()
    return render(request, "polls/reusl.html", {"q": q})