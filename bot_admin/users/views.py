from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User

@csrf_exempt
def setUser(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        try:
            user = User.objects.filter(tg_id=payload['id'])
        except:
            user = None
        # print('\n\n\n%s\n\n\n'%len(user))
        if len(user)==0:
            user = User(tg_id=payload['id'],
                        username=payload['username'],
                        first_name=payload['first_name'],
                        last_name=payload['last_name'])
            user.save()
        else:
            user.update(username=payload['username'],
                        first_name=payload['first_name'],
                        last_name=payload['last_name'])

        return HttpResponse("OK")

