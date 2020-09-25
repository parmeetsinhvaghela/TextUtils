# from django.http import HttpResponse
# from django.shortcuts import render
#
#
# def index(request):
#     return render(request,'index.html')
#     #return HttpResponse("<a href ="">Home</a>")
# #
# #     elif charcount == "on":
# #         charcount = 0
# #         analyzed = ""
# #         for char in data:
# #             if char != " ":
# #                charcount += 1
# #
# #         params = {'purpose': 'character count', 'analyzed_text': charcount}
# #         return render(request, 'analyze.html', params)
# #     else:
# #         return HttpResponse("Error")
# #
#
#
# def analyze(request):
#     #POST the text
#     djtext = request.POST.get('text', 'default')
#
#     # Check checkbox values
#     removepunc = request.POST.get('removepunc', 'off')
#     fullcaps = request.POST.get('fullcaps', 'off')
#     newlineremover = request.POST.get('newlineremover', 'off')
#     extraspaceremover = request.POST.get('extraspaceremover', 'off')
#
#     #Check which checkbox is on
#     if (removepunc == "on"):
#         punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#         analyzed = ""
#         for char in djtext:
#             if char not in punctuations:
#                 analyzed = analyzed + char
#         params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
#         djtext = analyzed
#         # return render(request, 'analyze.html', params)
#
#     if(fullcaps=="on"):
#         analyzed = ""
#         for char in djtext:
#             analyzed = analyzed + char.upper()
#
#         params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
#         djtext = analyzed
#         # Analyze the text
#         # return render(request, 'analyze.html', params)
#
#     if (extraspaceremover == "on"):
#         analyzed = ""
#         for index, char in enumerate(djtext):
#             if not (djtext[index] == " " and djtext[index + 1] == " "):
#                 analyzed = analyzed + char
#
#         params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
#         djtext = analyzed
#         # Analyze the text
#         # return render(request, 'analyze.html', params)
#
#     if (newlineremover == "on"):
#         analyzed = ""
#         for char in djtext:
#             if char != "\n" and char != "\r":
#                 analyzed = analyzed + char
#
#         params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
#
#     if (removepunc != "on" and fullcaps != "on" and extraspaceremover !="on" and newlineremover != "on"):
#         return HttpResponse("Error")
#


from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")


def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')


    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')


    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)

