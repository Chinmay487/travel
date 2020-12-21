from django.shortcuts import render,redirect
from .models import Feedback,CustomerQuery
from management.models import Destination



# Create your views here.
def index(request):
    
    dest = Destination.objects.all()
    return render(request,'index.html',{'title':'Home','dest':dest})

def review(request):
    feedbacks = Feedback.objects.all()
    return render(request,'reviews.html',{'feedbacks':feedbacks,'title':'review'})

def feedback(request):
    return render(request,'feedback.html',{'title':'give feedback'})

def submit_feedback(request):
    fed = Feedback() 
    fed.name = request.POST['name']
    fed.email = request.POST['email']
    fed.contact = request.POST['contact']
    fed.city = request.POST['city']
    fed.client_feedback = request.POST['feedback']
    fed.save()

    return redirect('/')

def about(request):
    return render(request,'about.html',{'title':'about us'})

def ask(request):
    dest = Destination.objects.all()
    return render(request,'ask.html',{'title':'Ask','dest':dest})

def submit_query(request):
    query = CustomerQuery()
    query.name=request.POST['name']
    query.email=request.POST['email']
    query.contact=request.POST['contact']
    query.destination=request.POST['destination']
    query.city=request.POST['city']
    query.save()
    return redirect('/')