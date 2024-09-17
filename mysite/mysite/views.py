from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("hello Guys")

def home(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text from the request
    djtext = request.POST.get('text', 'default')

    # Get the checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    counter = request.POST.get('counter', 'off')

    analyzed = djtext  # Start with the original text

    # Check if 'removepunc' is on
    if removepunc == 'on':
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ''.join([char for char in analyzed if char not in punctuations])

    # Check if 'uppercase' is on
    if uppercase == 'on':
        analyzed = analyzed.upper()

    # Check if 'counter' is on
    if counter == 'on':
        char_count = len(analyzed)
        analyzed += f'\nNumber of characters in your text is: {char_count}'

    # If no checkbox is selected, return an error message
    if removepunc != 'on' and uppercase != 'on' and counter != 'on':
        return HttpResponse("Error Occurred")

    # Pass the analyzed text to the template
    params = {'purpose': 'Text Analysis', 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)
