from .models import mode

def current_user_articles_processor(request):
    user = request.user
    current_user_articles = mode.objects.filter(editor__username=user).order_by('-created_on')
    return {'current_user_articles':current_user_articles}
