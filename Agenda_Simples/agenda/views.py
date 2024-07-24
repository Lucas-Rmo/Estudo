from django.shortcuts import render, get_object_or_404
from .models import Contato
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

def contatos(request):
    context = {"contatos":Contato.objects.all()}
    return render(request,"agenda/contato_list.html",context)

class Listar_Contato(ListView):
    model = Contato
    template_name = "agenda/contato_list.html"
    context_object_name = "contatos"

class Criar_Contato(CreateView):
    model = Contato
    template_name = "agenda/contato_form.html"
    fields = ["nome","telefone","email","resumo"]
    success_url = reverse_lazy("Listar_contatos")
    
class Atualizar_Contato(UpdateView):
    model = Contato
    template_name = "agenda/contato_form.html"
    fields = ["nome","telefone","email","resumo"]
    success_url = reverse_lazy("Listar_contatos")

class Deletar_Contato(DeleteView):
    model = Contato
    template_name = "agenda/contato_confirm_delete.html"
    success_url = reverse_lazy("Listar_contatos")


def detalhes_contato(request,pk):
    contato = get_object_or_404(Contato,pk=pk)
    return render(request,"agenda/detalhes_contato.html",{"contato":contato})