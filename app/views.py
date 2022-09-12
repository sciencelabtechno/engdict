from django.shortcuts import render
from pydictionary import Dictionary
# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def search_word(request):
    word=request.GET.get('word')
    x=Dictionary(word)
    m=str(x.meanings())
    m=m[1:len(m)-1]
    if(len(m)==0):
        m='No meaning found'

    a=str(x.antonyms())
    a=a[1:len(a)-1]
    if(len(a)==0):
        a='No anatonyms found'

    s=str(x.synonyms())
    s=s[1:len(s)-1]
    if(len(s)==0):
        s='No anatonyms found'

    dict1={'key1':word, 'key2':m, 'key3':a, 'key4':s}
    return render(request, 'app/result.html', dict1)