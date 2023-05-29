from collections import UserDict, UserList
from email.mime import image
from importlib.metadata import requires
from itertools import chain
from multiprocessing import context
from site import USER_BASE
from urllib import request
from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . models import *
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views import generic

from django.core.mail import send_mail



import requests

from isodate import parse_duration

from django.conf import settings
from django.shortcuts import render, redirect


# Create your views here.
@login_required(login_url='signin')
def index(request):
    courses = Course.objects.all()
    request_courches = Requested_course.objects.all()
    context = {
        'request_courches': request_courches,
    }
    return render(request, 'index.html', context)
    


# class Requested_courch_details(generic.DetailView):
#     model = Requested_course


def requested_courch_details(request, pk):
    courch_details = Requested_course.objects.get(id=pk)
    
    context = {
        'courch_details':courch_details
    }
    return render(request, 'courch_details.html', context)


def deletecourch(request, pk):
     courchDelet = Requested_course.objects.get(id=pk)
     courchDelet.delete()
     return redirect('index')





def about(request):
    return render(request, 'about.html')

@login_required(login_url='signin')
def banglaShikhi(request):
    bangla = BanglaLesson.objects.all()
    context = {
        'bangla': bangla
    }
    return render(request, 'bangla_shikhi.html', context)




@login_required(login_url='signin')
def sorborno(request):
    return render(request, 'sorborno.html')



@login_required(login_url='signin')
def banjonborno(request):
    return render(request, 'banjonborno.html')




@login_required(login_url='signin')
def englishAlphabet(request):
    return render(request, 'englishAlphabet.html')



@login_required(login_url='signin')
def capitalAlphabet(request):
    return render(request, 'capital-alphabet.html')



@login_required(login_url='signin')
def smallAlphabet(request):
    return render(request, 'smallAlphabet.html')




@login_required(login_url='signin')
def অংক_শিখি(request):
    return render(request, 'অংক_শিখি.html')




@login_required(login_url='signin')
def বাংলা_সংখ্যা(request):
    return render(request, 'বাংলা_সংখ্যা.html')




@login_required(login_url='signin')
def নামতা(request):
    return render(request, 'নামতা.html')


@login_required(login_url='signin')
def নামতা_1(request):
    return render(request, '1এর_নামতা.html')


@login_required(login_url='signin')
def নামতা_2(request):
    return render(request, '2এর_নামতা.html')


@login_required(login_url='signin')
def নামতা_3(request):
    return render(request, '3এর_নামতা.html')


@login_required(login_url='signin')
def নামতা_4(request):
    return render(request, '4এর_নামতা.html')


@login_required(login_url='signin')
def নামতা_5(request):
    return render(request, '5এর_নামতা.html')


@login_required(login_url='signin')
def নামতা_6(request):
    return render(request, '6এর_নামতা.html')


@login_required(login_url='signin')
def নামতা_7(request):
    return render(request, '7এর_নামতা.html')


@login_required(login_url='signin')
def নামতা_8(request):
    return render(request, '8এর_নামতা.html')


@login_required(login_url='signin')
def নামতা_9(request):
    return render(request, '9এর_নামতা.html')


@login_required(login_url='signin')
def নামতা_10(request):
    return render(request, '10এর_নামতা.html')



@login_required(login_url='signin')
def englishNumbers(request):
    return render(request, 'englishNumbers.html')



@login_required(login_url='signin')
def kobita(request):
    return render(request, 'kobita.html')



@login_required(login_url='signin')
def banglakobita(request):
    videos = []

    if request.method == 'POST':
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        video_url = 'https://www.googleapis.com/youtube/v3/videos'

        search_params = {
            'part' : 'snippet',
            'q' : request.POST['search'],
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'maxResults' : 9,
            'type' : 'video'
        }

        r = requests.get(search_url, params=search_params)

        results = r.json()['items']
        
        video_ids = []
        for result in results:
            video_ids.append(result['id']['videoId'])

        if request.POST['submit'] == 'lucky':
            return redirect(f'https://www.youtube.com/watch?v={ video_ids[0] }')

        video_params = {
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'part' : 'snippet,contentDetails',
            'id' : ','.join(video_ids),
            'maxResults' : 9
        }

        r = requests.get(video_url, params=video_params)

        results = r.json()['items']

        
        for result in results:
            video_data = {
                'title' : result['snippet']['title'],
                'id' : result['id'],
                'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
                'duration' : int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
                'thumbnail' : result['snippet']['thumbnails']['high']['url']
            }

            videos.append(video_data)

    context = {
        'videos' : videos
    }


    return render(request, 'বাংলা_কবিতা.html', context)


@login_required(login_url='signin')
def englishPoem(request):
    videos = []

    if request.method == 'POST':
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        video_url = 'https://www.googleapis.com/youtube/v3/videos'

        search_params = {
            'part' : 'snippet',
            'q' : request.POST['search'],
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'maxResults' : 9,
            'type' : 'video'
        }

        r = requests.get(search_url, params=search_params)

        results = r.json()['items']
        
        video_ids = []
        for result in results:
            video_ids.append(result['id']['videoId'])

        if request.POST['submit'] == 'lucky':
            return redirect(f'https://www.youtube.com/watch?v={ video_ids[0] }')

        video_params = {
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'part' : 'snippet,contentDetails',
            'id' : ','.join(video_ids),
            'maxResults' : 9
        }

        r = requests.get(video_url, params=video_params)

        results = r.json()['items']

        
        for result in results:
            video_data = {
                'title' : result['snippet']['title'],
                'id' : result['id'],
                'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
                'duration' : int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
                'thumbnail' : result['snippet']['thumbnails']['high']['url']
            }

            videos.append(video_data)

    context = {
        'videos' : videos
    }

    return render(request, 'english_poem.html', context)






@login_required(login_url='signin')
def quizlist(request):
    return render(request, 'allquizlist.html')




def mathquiz(request):
    return render(request, 'mathquiz.html')

def subtract(request):
    return render(request, 'subtract.html')


def multiply(request):
    return render(request, 'multiply.html')


def divide(request):
  return  render(request, 'divide.html')



def shadaron_gan_quiz(request):
    return render(request, 'shadaron_gen_quiz.html')



def colorquiz(request):
    return render(request, 'colorquiz.html')





def paint(request):
    return render(request, 'paint.html')



def contact(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }
        message = '''
        New message: {}

        From: {}
        '''.format(data['message'], 
        data['email'])
        send_mail(data['subject'], 
        message, '', 
        ['moklasur15-2284@diu.edu.bd'])

        contact.name=name
        contact.email=email
        contact.subject=message

        contact.save()
        return HttpResponse("<h2>Thank for your message We will respond soon</h2>")



        
    return render(request, 'contactus.html', {})









def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signin')
          
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signin')
           
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signin')
        
    else: 
        return render(request,'signup.html')



def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'credentials Invalid')
            return redirect('signin')
    
    else:
        return render(request, 'signin.html')




@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')