from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def path_assessment(request):
    return HttpResponse("Here's the text of the web page.")

def other_function(request):
    return HttpResponse("This is a website page.")

def main_page(request):


   
    class Point:
        def __init__(self, name) -> None:
            self.name = name
            self.path="http://127.0.0.1:8000/assessment"
            
        
            
    dcit0 = {
        'City_services': {
            'Assessment': {
                'Buildinganddevelopment': 0
            }
        }
    }    
            
    
    point_1 = Point('task')
    point_2 = Point('task2')
    point_3 = Point('task3')
    context = {
        'core': [point_1, ],
        'core1': [point_2,],
        'core2':[point_3],
    }
    return render(request, 'menu.html', context)


def add_functional_to_words(req):
    pass

'''
Сделать меню по картинке

сделать ссылки по тегам
'''