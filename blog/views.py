from django.shortcuts import redirect, render, get_object_or_404
from .models import Blog
from .forms import BlogForm
# View to show all blog posts
def blog_list(request):
    blogs = Blog.objects.all()  # Fetch all blog posts from database
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

# View to show a single blog post
def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)  # Get blog by ID or show 404 if not found
    return render(request, 'blog/blog_detail.html', {'blog': blog})
def add_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')  # redirect to list view after saving
    else:
        form = BlogForm()
    return render(request, 'blog/add_blog.html', {'form': form})