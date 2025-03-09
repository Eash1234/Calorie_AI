from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from .models import ChatMessage
from .ai_service import AIService


def index(request):
    """Render the single page application"""
    return render(request, 'chatbot/index.html')


@csrf_exempt
def user_login(request):
    """Handle user login"""
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        # Fixed username and password for simplicity
        # In a real application, you should use proper authentication
        if username == 'konvi' and password == 'konvi2025':
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid credentials'})
    return JsonResponse({'success': False, 'message': 'Method not allowed'})


@csrf_exempt
def chat(request):
    """Handle chat requests"""
    if request.method == 'POST':
        data = json.loads(request.body)
        user_input = data.get('message')

        # Generate response
        ai_service = AIService()
        bot_response = ai_service.generate_response(user_input)

        # Store in database
        ChatMessage.objects.create(
            user_input=user_input,
            bot_response=bot_response
        )

        return JsonResponse({
            'success': True,
            'response': bot_response
        })
    else:
        return JsonResponse({'success': False, 'message': 'Method not allowed'})


@csrf_exempt
def get_chat_history(request):
    """Get chat history from database"""
    messages = ChatMessage.objects.all().order_by('-timestamp')[:50]  # Get last 50 messages
    history = []
    for msg in messages:
        history.append({
            'user_input': msg.user_input,
            'bot_response': msg.bot_response,
            'timestamp': msg.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        })
    return JsonResponse({'success': True, 'history': history})