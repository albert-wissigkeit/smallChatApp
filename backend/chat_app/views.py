import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt  # Um CSRF-Fehler zu vermeiden

from chat_app.models import Chat

# Create your views here.

@csrf_exempt  # Diese Dekoration deaktiviert CSRF-Prüfung für diese View
def chat_view(request):
    if request.method == "GET":
        chat_data = Chat.objects.all().values('name', 'message', 'created_at')  
        # ruft alle Chat-Objekte ab und verwendet `values`, um nur die Felder 'name', 'message' und 'created_at' auszuwählen. 
        # `values()` gibt ein QuerySet zurück, das eine Liste von Dictionaries enthält.
        
        return JsonResponse(list(chat_data), safe=False)  
        # Mit `list()` wird das QuerySet `chat_data` in eine reguläre Python-Liste umgewandelt, die JSON-kompatibel ist.
        # Wenn man eine Liste anstatt eines Dictionaries zurückgibt, muss `safe=False` gesetzt werden, 
        # da `JsonResponse` standardmäßig nur ein Dictionary akzeptiert.
    
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Konvertiert die JSON-Daten in ein Python Dictionary
            name = data.get('name')
            message = data.get('message')

            if not name or not message:
                return JsonResponse({'error': 'Name und Nachricht sind erforderlich!'}, status=400)
            
            new_chat = Chat.objects.create(name=name, message=message)
            return JsonResponse({'message': 'Nachricht erfolgreich gespeichert!', 'id': new_chat.id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Ungültige JSON-Daten!'}, status=400)
