from django.shortcuts import render
from twilio.rest import Client

# Create your views here.

def home(request):


    return render(request, 'twit/home.html')

def status(request):
    phone = request.GET.get('phone')
    message = request.GET.get('message')
    account_sid = 'AC084b5641a2435e72c3e1e894cf57db18'
    auth_token = '5900504d34f0a41ce842b2ab9c91af5a'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=f'{message}',
            from_='+12013791613',
            to=f"{phone}"
        )

    print(message.sid)
    return render(request, 'twit/status.html')