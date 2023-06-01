from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import CodingQuestion, UserCodingQuestion
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@login_required
def courses(request):
    questions = CodingQuestion.objects.all()
    if request.GET:
        difficulty=request.GET.get('difficulty')
        topic=request.GET.get('topic')
    else:
        difficulty=topic='All'
    return render(request,'courses/courses.html',{ 'questions':questions,'difficulty': difficulty, 'topic': topic })

@csrf_exempt
def question_status_update(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')
        is_done = request.POST.get('is_done')
        question = CodingQuestion.objects.get(pk=pk)
        user_question, created = UserCodingQuestion.objects.get_or_create(
            user=request.user,
            question=question,
        )
        user_question.is_done = is_done
        user_question.save()
        return JsonResponse({'success': True, 'is_done': user_question.is_done}, status=200)
    else:
        return JsonResponse({'success': False, 'errors': []}, status=400)
    
