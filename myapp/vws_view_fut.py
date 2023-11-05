from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def view_fut_in_progress(request):
    return render(request, 'view_fut/futs/in-progress.html')


@login_required
def view_fut_finished(request):
    return render(request, 'view_fut/futs/finished.html')