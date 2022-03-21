from django.http import HttpResponse
from django.template import Template, Context, loader #importing libraries

def start(request): #main view

    
    plt=loader.get_template('main.html')#Getting HTML view
    

    ctx={
        'name':'Joced'
    }#Vars and Functions

    document=plt.render(ctx)

    return HttpResponse(document)