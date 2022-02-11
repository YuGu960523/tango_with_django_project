from django.shortcuts import render

from django.http import HttpResponse
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm,PageForm
from django.shortcuts import redirect


def index(request):

    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    page_list = Page.objects.order_by('-views')[:5]
    context_dict['pages'] = page_list

    return render(request, 'rango/index.html', context=context_dict)
def about(request):
# prints out whether the method is a GET or a POST
    print(request.method)
# prints out the user name, if no one is logged in it prints `AnonymousUser`
    print(request.user)
    return render(request, 'rango/about.html', {})

def show_category(request, category_name_slug):

    context_dict = {}
    try:

        category = Category.objects.get(slug=category_name_slug)

        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages

        context_dict['category'] = category
    except Category.DoesNotExist:

        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context=context_dict)

def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        
        if form.is_valid():
         
            category = form.save(commit=True)
            print(category, category.slug)
           
            return index(request)
        else:
   
            print(form.errors)
 
    return render(request, 'rango/add_category.html', {'form': form})

def add_page(request, category_name_slug):
    try:
            category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
            category = None
    if category is None:
        return redirect('/rango/')
    
    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
        return show_category(request, category_name_slug)
    else:
            print(form.errors)
      
    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context=context_dict)


