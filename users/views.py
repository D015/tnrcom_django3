from django.shortcuts import render


def index(request):


    context = {
        'posts': posts,
        # 'cats': cats,
        # 'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context)
