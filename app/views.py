from django.shortcuts import render
from .models import RegUser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
    print(request.GET)
    print("HAHA")
    if request.POST:
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        # del request.POST
        x = RegUser.objects.create(name=name, phone_number = phone_number, email_address = email)
        x.save()
        print("done registering")
        print(name, phone_number, email)
        # request.GET =

    return render(request, 'app/index.html')
