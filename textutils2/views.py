#this file is created by - Manish
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")
##=====================================================================##
def analyze(request):
    #Getting Text
    user_text=request.POST.get("mytext","default")
    #Check box value - Punctuation
    user_punc=request.POST.get("remove_punc","off")
    #Check box value - Uppercase
    user_uppercase=request.POST.get("uppercase","off")
    #Check box value - New Line Remover
    new_line_remover=request.POST.get("line_remover","off")
    #Check box value - Extra Space Remover
    extra_space_remover=request.POST.get("space_remover","off")
    #Check box value - Character Counters
    character_counter=request.POST.get("character_counter","off")
    print(user_text)
    #Blank string for all purpose:
    a_text = ""
    ##=================================================================##
    if user_punc=="on":
        punctuation="""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        for char in user_text:
            if char not in punctuation:
                a_text=a_text+char
        dict = {"purpose": "Remove Punctuation", "analyze_text": a_text}
        return render(request, "analyze.html", dict)
    ##================================================================##
    elif user_uppercase=='on':
        for char in user_text:
            a_text=a_text+char.upper()
        dict={"purpose":"uppercase","analyze_text":a_text}
        return render(request,"analyze.html",dict)
    ##================================================================##
    elif new_line_remover=="on":
        for char in user_text:
            if char!="\n" and char!="\r":
                a_text=a_text+char
        print(a_text)
        dictss={"purpose":"New Line Remover","analyze_text":a_text}
        return render(request,"analyze.html",dictss)

    ##================================================================##
    elif extra_space_remover=="on":
        for index,char in enumerate(user_text):
            if user_text[index]==" " and user_text[index+1]==" ":
                pass
            else:
                a_text=a_text+char

        dict={"purpose":"Extra Space Remover","analyze_text":a_text}
        return render(request,"analyze.html",dict)
    ##================================================================##

    elif character_counter=="on":
        te_l = []
        for char in user_text:
                if not char.isspace():
                    te_l.append(char)

        dict = {"purpose": "Character Counts", "analyze_text": len(te_l),"note_charcount":"Note : Only characater will be counts and space will be ignore."}
        return render(request, "analyze.html", dict)
    ##================================================================##

    else:
        return HttpResponse("Error in parsing")

    ##================================================================##