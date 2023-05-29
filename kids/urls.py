from unicodedata import name
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courch_details/<int:pk>', views.requested_courch_details, name='courch-details' ),
    path('courch_delete/<int:pk>', views.deletecourch, name='deletecourch'),

    
    # path('courch_details/<int:pk>', views.Requested_courch_details.as_view(), name='courch-details'),

    
    
    path('bangla', views.banglaShikhi, name='bangla'),
    path('sorborno', views.sorborno, name='sorborno'),
    path('banjonborno', views.banjonborno, name='banjonborno'),
    path('englishAlphabet', views.englishAlphabet, name='englishAlphabet'),
    path('capitalAlphabet', views.capitalAlphabet, name='capitalAlphabet'),
    path('smallAlphabet/', views.smallAlphabet, name='smallAlphabet'),
    path('অংক-শিখি', views.অংক_শিখি, name='অংক-শিখি'),
    path('বাংলা_সংখ্যা', views.বাংলা_সংখ্যা, name='বাংলা_সংখ্যা'),
    path('নামতা', views.নামতা, name='নামতা'),
    
    path('1_এর_নামতা', views.নামতা_1, name='1_এর_নামতা'),
    path('2_এর_নামতা', views.নামতা_2, name='2_এর_নামতা'),
    path('3_এর_নামতা', views.নামতা_3, name='3_এর_নামতা'),
    path('4_এর_নামতা', views.নামতা_4, name='4_এর_নামতা'),
    path('5_এর_নামতা', views.নামতা_5, name='5_এর_নামতা'),
    path('6_এর_নামতা', views.নামতা_6, name='6_এর_নামতা'),
    path('7_এর_নামতা', views.নামতা_7, name='7_এর_নামতা'),
    path('8_এর_নামতা', views.নামতা_8, name='8_এর_নামতা'),
    path('9_এর_নামতা', views.নামতা_9, name='9_এর_নামতা'),
    path('10_এর_নামতা', views.নামতা_10, name='10_এর_নামতা'),
    
    path('about', views.about, name='about'),
    
    path('englishNumbers', views.englishNumbers, name='englishNumbers'),
    
    path('kobita', views.kobita, name='kobita'),
    path('banglakobita', views.banglakobita, name='banglakobita'),
    path('englishPoem', views.englishPoem, name='englishPoem'),

    path('quizlist', views.quizlist, name="quizlist"),
    path('mathquiz', views.mathquiz, name='mathquiz'),
    
    path('subtract', views.subtract, name='subtract'),
    path('multiply', views.multiply, name='multiply'),
    path('divide', views.divide, name='divide'),
    path('sadarongen', views.shadaron_gan_quiz, name='sadarongen'),
    path('colorquiz', views.colorquiz, name='colorquiz'),
    path('paint', views.paint, name='paint'),

    path('contact', views.contact, name='contact'),
    










    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name="signin"),
    path('logout', views.logout, name='logout'),

    


]