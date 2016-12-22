from django.shortcuts import render
from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse

from .models import Judge
from .models import Entry
from .models import Photo
from .forms import LoginForm

def get_entries_dict(judge):
    entries = []
    for _entry in Entry.objects.filter(judge=judge):
        entry = {
            'id': _entry.id,
            'title': _entry.title,
            'rank': _entry.rank
        }
        photos = []
        for _photo in Photo.objects.filter(entry=_entry):
            photos.append({
                'order': _photo.order,
                'thumbnail_url': _photo.thumbnail_url,
                'full_size_url': _photo.full_size_url
            })
        entry['photos'] = sorted(photos, key=lambda k: k['order'])
        entries.append(entry)
    return sorted(entries, key=lambda k: k['rank']) 

def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                judge = Judge.objects.get(
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password']
                    )
            except Judge.DoesNotExist as e:
                return render(request, 'login.html', {'error_message': 'Your email or password is invalid', 'form': form})
            request.session['judge'] = judge.id
            request.session.modified = True
        else:
            return render(request, 'login.html', {'error_message': 'Invalid inputs', 'form': form})
    if 'judge' in request.session:
        return redirect('view_entries')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def view_entries(request):
    judge = Judge.objects.get(id=request.session['judge'])
    entries = get_entries_dict(judge)
    return render(request, 'view_entries.html', {
        'judge': judge,
        'entries': entries
    })

def logout(request):
    if 'judge' in request.session:
        del request.session['judge']
        request.session.modified = True
    return redirect('index')

def save(request):
    if request.method == 'POST':
        judge = Judge.objects.get(id=request.session['judge'])
        for entry in Entry.objects.filter(judge=judge):
            if '%s' % entry.id in request.POST:
                new_rank = request.POST['%s' % entry.id]
                entry.rank = new_rank
                entry.save()
        entries = get_entries_dict(judge)
        return render(request, 'save.html', {
            'judge': judge,
            'entries': entries
        })
    else:
        return redirect('index')