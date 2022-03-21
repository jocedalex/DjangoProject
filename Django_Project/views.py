from django.http import HttpResponse
from django.template import Template, Context #importing libraries

def start(request): #main view

    with open("D:/Documentos/Python/Python 2 Project/Django_Project/Django_Project/html/main.html") as ext_path:
        plt=Template(ext_path.read())#Getting HTML view
    

    ctx=Context({
        'name':'Joced'
    })#Vars and Functions

    document=plt.render(ctx)

    return HttpResponse(document)