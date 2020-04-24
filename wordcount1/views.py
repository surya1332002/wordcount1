import operator

from django.shortcuts import render


def home(request):
    return render(request, 'home/home.html')


def count(request):
    fulltext = request.GET['fulltext']

    word_list = fulltext.split()

    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            # increase
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    x = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'home/count.html',
                  {'fulltext': fulltext,
                   'count': len(word_list),
                   'word_dictionary': x
                   })


def about(request):
    return render(request, 'home/about.html')
