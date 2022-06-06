from django.shortcuts import render , redirect
from .models import Chat

# Create your views here.
def home(request):
    chats = Chat.objects.all()
    return render(request,'chatbox/message.html',{ 'chats': chats })

def send(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        chat = Chat(message=message)
        chat.save()
        return redirect('home')



    return render(request,'chatbox/message.html')