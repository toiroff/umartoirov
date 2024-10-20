from django.shortcuts import render,redirect
from .models import About,Resume,Skill,Project,Blog,Comment
from .forms import CommentForm,ContactForm


# Create your views here.
def index(request):
  about = About.objects.first()
  resumes = list(Resume.objects.all())   
  skills = Skill.objects.all()
  projects = Project.objects.all()
  blog = Blog.objects.all()

  form = ContactForm()

  if request.method == 'POST':
     form = ContactForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect('home')
     
     else:
      print(form.errors)
    
  odds = resumes[::2] 
  evens = resumes[1::2]

  contex = {
    'about':about,
    'resume_right':evens,
    'resume_left':odds,
    'skills':skills,
    'projects':projects,
    'blog':blog,
    'form':form
  }
  return render(request, 'index.html', contex)

def blog(request,slug):
  blog = Blog.objects.get(slug=slug)
  recent = Blog.objects.all()[:4]
  form = CommentForm()

  if request.method == 'POST':
      form = CommentForm(request.POST)
      if form.is_valid():
          comment = form.save(commit=False)
          comment.blog = blog
          comment.save()
          return redirect('blog', slug=blog.slug)
      else:
          print(form.errors)

  content = {
      'blog':blog,
      'recent':recent,
      'form':form
      }

  return render(request,'single.html',content)