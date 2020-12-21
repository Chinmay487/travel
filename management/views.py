from django.shortcuts import render,redirect
from client.models import Feedback,CustomerQuery
from .models import Destination
from django.contrib.auth.models import auth,User


# Create your views here.
def management_index(request):
    
    if request.user.is_authenticated :
        dest = Destination.objects.all()
        return render(request,'manage_index.html',{'title':'index','dest':dest})
    return redirect('/login/')



def review(request):
    if request.user.is_authenticated :
        feedbacks = Feedback.objects.all()
        return render(request,'manage_review.html',{'title':'reviews','feedbacks':feedbacks})
    return redirect('/')

def delete_review(request):
    if request.user.is_authenticated :
        fname = request.POST['customer_id']
        feedback = Feedback.objects.get(name=fname)
        feedback.delete()
        return redirect('/manage/review')
    return redirect('/')

def add_dest(request):
    if request.user.is_authenticated :
        return render(request,'manage_addDest.html',{'title':'add destination'})
    return redirect('/')

def add_new_dest(request):
    if request.user.is_authenticated :
        dest = Destination()
        dest.name=request.POST['dest_name']
        dest.description=request.POST['dest_description']
        dest.price=request.POST['dest_price']
        dest.image=request.FILES['destImg']
        dest.save()
        return redirect('/manage')
    return redirect('/')

def delete_data(request):
    if request.user.is_authenticated :
        destId = request.POST['destId']
        dest = Destination.objects.get(id=destId)
        dest.delete()
        return redirect('/manage')
    return redirect('/')

def query(request):
    if request.user.is_authenticated :
        query = CustomerQuery.objects.all()
        return render(request,'manage_query.html',{'title':'customer queries','query':query})
    return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect('/')
