from django.http import HttpResponse
from .models import Message


def getMessage(request):
	message = Message.objects.first()
	return HttpResponse(message.text)
