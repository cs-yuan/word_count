from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def count(request):
    count_num = len(request.GET['hello'])
    text = request.GET['hello']
    dic = {'hell': count_num,'text':text}
    dict = {}
    for word in text:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1
    max_char = text[0]
    for key in dict:
        if dict[key]>dict[max_char]:
            max_char = key
    dic['max_char'] = max_char
    dic['max_num']  = dict[max_char]
    return render(request, 'count.html', dic)
