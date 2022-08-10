from dataclasses import field
from django.shortcuts import render
from .models import MathWord, PCWord, SVTWord
from .filters import OrderFilter


def home(request):

    return render(request,'home.html')

# Physics & Chemistry :

def pc(request):
    
    return render(request,'pc/pc.html')

def pc_general(request):

    general_words = PCWord.objects.all().filter(field='General')
    filter = OrderFilter(request.GET,queryset=general_words)
    general_words = filter.qs
    context = {
        'general_words':general_words,
        'filter':filter,
    }

    return render(request,'pc/pc_general.html',context)

def pc_mechanics(request):

    general_words = PCWord.objects.all().filter(field='General')
    filter = OrderFilter(request.GET,queryset=general_words)
    general_words = filter.qs
    context = {
        'general_words':general_words,
        'filter':filter,
    }

    return render(request,'pc/pc_general.html',context)

def pc_electricity(request):

    electricity_words = PCWord.objects.all().filter(field='Electricity')
    filter = OrderFilter(request.GET,queryset=electricity_words)
    electricity_words = filter.qs
    context = {
        'electricity_words':electricity_words,
        'filter':filter,
    }

    return render(request,'pc/electricity.html',context)

def pc_optics(request):

    optics_words = PCWord.objects.all().filter(field='Optics')
    filter = OrderFilter(request.GET,queryset=optics_words)
    optics_words = filter.qs
    context = {
        'optics_words':optics_words,
        'filter':filter,
    }

    return render(request,'pc/optics.html',context)

def pc_waves(request):

    waves_words = PCWord.objects.all().filter(field='Waves')
    filter = OrderFilter(request.GET,queryset=waves_words)
    waves_words = filter.qs
    context = {
        'waves_words':waves_words,
        'filter':filter,
    }

    return render(request,'pc/general.html',context)

def pc_nuclear(request):

    nuclear_words = PCWord.objects.all().filter(field='Nuclear transformation')
    filter = OrderFilter(request.GET,queryset=nuclear_words)
    nuclear_words = filter.qs
    context = {
        'nuclear_words':nuclear_words,
        'filter':filter,
    }

    return render(request,'pc/nuclear.html',context)

def pc_matter(request):

    matter_words = PCWord.objects.all().filter(field='Matter')
    filter = OrderFilter(request.GET,queryset=matter_words)
    matter_words = filter.qs
    context = {
        'matter_words':matter_words,
        'filter':filter,
    }

    return render(request,'pc/matter.html',context)

def pc_measurement(request):

    measurement_words = PCWord.objects.all().filter(field='Measurements in chemistry')
    filter = OrderFilter(request.GET,queryset=measurement_words)
    measurement_words = filter.qs
    context = {
        'measurement_words':measurement_words,
        'filter':filter,
    }

    return render(request,'pc/measurement.html',context)

def pc_reactions(request):

    reactions_words = PCWord.objects.all().filter(field='Chemical reactions')
    filter = OrderFilter(request.GET,queryset=reactions_words)
    reactions_words = filter.qs
    context = {
        'reactions_words':reactions_words,
        'filter':filter,
    }

    return render(request,'pc/reactions.html',context)

def pc_organic(request):

    organic_words = PCWord.objects.all().filter(field='Organic chemistry')
    filter = OrderFilter(request.GET,queryset=organic_words)
    organic_words = filter.qs
    context = {
        'organic_words':organic_words,
        'filter':filter,
    }

    return render(request,'pc/organic.html',context)
    
# SVT :

def svt(request):
    
    return render(request,'svt/svt.html')

def svt_general(request):

    general_words = SVTWord.objects.all().filter(field='General')
    filter = OrderFilter(request.GET,queryset=general_words)
    general_words = filter.qs
    context = {
        'svt_general_words':general_words,
        'filter':filter,
    }

    return render(request,'svt/svt_general.html',context)