from django.shortcuts import render
from django.utils import timezone
from diary.models import Diary
from django.shortcuts import render, redirect, get_object_or_404
from diary.models import *

def home(request):
    diary=Diary.objects.all()
    return render(request, 'home.html', {'diary':diary})

def create(request):
    # 글을 작성할 경우 POST 방식
    if request.method == "POST":
        new_diary=Diary()
        new_diary.title=request.POST['title']
        new_diary.pub_date=timezone.datetime.now()
        new_diary.mood=request.POST['mood']
        new_diary.weather=request.POST['weather']
        new_diary.body=request.POST['body']
        new_diary.image=request.FILES['image']
        
        '''
        # 글을 작성한(로그인한 user의 id) user의 id를 user_id 변수에 저장
        user_id=request.user.id
        # user_id 값과 User 모델의 객체 중 일치하는 값을 저장
        user = User.objects.get(id=user_id)
        # 작성자 = user
        new_board.author=user
        '''
        
        # db에 생성된 diary 객체 저장
        new_diary.save()
        return redirect('home')
        
    # 단순 create 페이지로 이동할 경우 GET 방식으로 들어감
    else:
        return render(request, 'new.html')

def detail(request, id):
    diary=get_object_or_404(Diary, pk=id)
    return render(request, 'detail.html', {'diary':diary})

def edit(request, id):
    if request.method=="POST":
        edit_diary=Diary.objects.get(id=id)
        edit_diary.title=request.POST['title']
        edit_diary.body=request.POST['body']
        edit_diary.save()
        return redirect('detail', edit_diary.id)
    else:
        diary=Diary.objects.get(id=id)
        return render(request, 'edit.html', {'diary':diary})
    
def delete(request,id):
    delete_diary=Diary.objects.get(id=id)
    delete_diary.delete()
    return redirect('home')