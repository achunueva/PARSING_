from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView, FormView
from . import models, forms


class ParserView(ListView):
    model = models.TvParser
    template_name = 'film_list.html'
    context_object_name = 'list'


class ParserFormView(FormView):
    template_name = 'parser_film.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('<h1>ГОТОВО</h1>')
        else:
            return super(ParserFormView, self).post(request, *args, **kwargs)
