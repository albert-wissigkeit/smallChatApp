from django.http import JsonResponse
from django.shortcuts import render

from chat_app.models import Chat

# Create your views here.
def chat_view(request):
    if request.method == "GET":
        chat_data = Chat.objects.all().values('name', 'message', 'created_at')  
        # ruft alle Chat-Objekte ab und verwendet `values`, um nur die Felder 'name', 'message' und 'created_at' auszuwählen. 
        # `values()` gibt ein QuerySet zurück, das eine Liste von Dictionaries enthält.
        
        return JsonResponse(list(chat_data), safe=False)  
        # Mit `list()` wird das QuerySet `chat_data` in eine reguläre Python-Liste umgewandelt, die JSON-kompatibel ist.
        # Wenn man eine Liste anstatt eines Dictionaries zurückgibt, muss `safe=False` gesetzt werden, 
        # da `JsonResponse` standardmäßig nur ein Dictionary akzeptiert.
