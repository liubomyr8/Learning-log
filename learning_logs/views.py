from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404, JsonResponse
from django.template.loader import render_to_string

from .models import Topic, Entry, Comment
from .forms import TopicForm, EntryForm, CommentForm

# Create your views here.
def index(request):
    """General page"""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    topics = Topic.objects.filter(is_private=False).order_by('date_added')
    my_topics = Topic.objects.filter(owner=request.user, is_private=True).order_by('date_added')
    context = {'topics': topics, 'my_topics': my_topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    
    if (topic.is_private == True):
        check_topic_owner(request, topic)
    
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
    
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(request, topic)
    
    if request.method != 'POST':
        form = EntryForm
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
        
    context = {"topic": topic, "form": form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(request, topic)
    
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

@login_required
def new_comment(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    _check_entry(request, entry, topic)
    
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.entry = entry
            new_comment.save()
            return redirect('learning_logs:public_entry', entry_id = entry_id)
    context = {"entry": entry, "form": form}
    return render(request, 'learning_logs/new_comment.html', context)

@login_required
def topics(request):
    topics = Topic.objects.filter(is_private=False).order_by('date_added')
    my_topics = Topic.objects.filter(owner=request.user, is_private=True).order_by('date_added')
    context = {'topics': topics, 'my_topics': my_topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def entry_comments(request):
    comments = Comment.objects.order_by('date_added')
    context = {'comments': comments}
    return render

@login_required
def get_comments(request):
    entry_id = request.GET.get('entry_id')
    entry = Entry.objects.get(pk=entry_id)
    comments = Comment.objects.filter(entry=entry)
    comments_html = render_to_string('comments.html', {'comments': comments})

    return JsonResponse({'comments': comments_html})
    
    

def check_topic_owner(request, topic):
    if topic.owner != request.user:
        raise Http404
    
def _check_entry(request, entry, topic):
    if (entry.owner != request.user) and (topic.is_private == True):
        raise Http404
            