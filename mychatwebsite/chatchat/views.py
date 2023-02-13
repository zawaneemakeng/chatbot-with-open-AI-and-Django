from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import openai


def Qa(request):
    qa = QA2.objects.all()
    context = {'qa': qa}
    openai.api_key = "your API key here!!"
    if request.method == 'POST':
        data = request.POST.copy()
        title = data.get('qa')
        print(title)
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=title,
            temperature=0.9,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
    )
        print("--------------------------------")
        qa2 = response['choices'][0]['text']
        print(qa2)
        print("--------------------------------")
        new_record = QA2()
        new_record.title = title
        new_record.qa = qa2
        new_record.save()
    return render(request, 'chat/home.html', context)
