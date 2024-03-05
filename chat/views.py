from django.shortcuts import render, redirect
from . models import Room


# def chatPage(request, *args, **kwargs):
# 	if not request.user.is_authenticated:
# 		return redirect("login-user")
# 	context = {}
# 	return render(request, "chat/chatPage.html", context)

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'chat/chat_list.html', {'rooms':rooms})

def room_view(request, room_name):
    chat_room, created = Room.objects.get_or_create(name=room_name)
    return render(request, 'chat/room.html', {'room': chat_room})

