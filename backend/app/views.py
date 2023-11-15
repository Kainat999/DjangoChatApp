from .models import Chat, Group
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


from django.shortcuts import render


def landing_page_view(request):
    
    return render(request, 'landing_page.html')



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def chat_rooms_static_view(request):
    return render(request, 'app/ChatRooms.html')


@login_required
def index(request, group_name):
    print("Group Name....", group_name)

    # filter group name 
    group = Group.objects.filter(name = group_name).first()
    chats=[]
    # condition for get chat 
    if group:
        chats = Chat.objects.filter(group=group)
    else:
        group = Group(name = group_name)
        group.save()
        
    return render(request, 'app/index.html', {'groupname':group_name, 'chats':chats})