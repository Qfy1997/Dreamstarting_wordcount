#from django.http import HttpResponse  #请求
from django.shortcuts import render #传递网页给用户


#def home(request):
#    return HttpResponse('hello Django')

def home2(request):
    return render(request, 'home.html')


def count(request):
    user_text=request.GET['text']
    totalcount=len(user_text)

    word_dict={}
    for word in user_text:
        if word not in word_dict:
            word_dict[word]=1
        else:
            word_dict[word]+=1
    sorted_dict=sorted(word_dict.items(),key=lambda w:w[1],reverse=True)
    return render(request,'count.html',
                {'total_count':totalcount,'text': user_text,'worddict':word_dict,'sorted':sorted_dict})


def about(request):
    return render(request,'about.html')