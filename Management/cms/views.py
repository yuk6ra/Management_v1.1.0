from django.shortcuts import render
from django.http import HttpResponse

from cms.models import Habit


def habit_list(request):
    """habit list"""
    # return HttpResponse('書籍の一覧')
    habits = Habit.objects.all().order_by('id')

    return render(request, 'cms/habit_list.html', {'habits': habits})


def habit_edit(request, habit_id=None):
    """habit edit"""
    return HttpResponse('習慣の編集')


def habit_del(request, habit_id):
    """習慣の削除"""
    return HttpResponse('習慣の削除')

