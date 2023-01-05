from django.urls import path
# import views
from .views import main_page, path_assessment, other_function




class MenuRow:
    def __init__(self, level:int, name:str, childs:dict):
        self.level = level
        self.name = name
        self.url = ''
        self.childs = childs




assessment = MenuRow(level=1, name='assessment', childs={})
building_and_development = MenuRow(level=1, name="buildinganddevelopment", childs={})

menu_root = MenuRow(level=0, name="CityServicies", childs={1: assessment, 2: building_and_development}) 


urlpatterns = [
    path('', main_page),    
]


# path('', views.path_assessment),
# path('Assessment', views.path_assessment),
# path('Building and Development', views.path_assessment),


for possition, next_row in menu_root.childs.items():
    print(possition, next_row.name)
    
    urlpatterns.append(path(next_row.name, main_page))
    
    
    
     
        

    
