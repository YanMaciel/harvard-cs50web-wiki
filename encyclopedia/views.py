from django.shortcuts import render, redirect
import random

import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.django-html", {
        "entries": util.list_entries()
    })

def wiki_detail_view(request, entry=None):
    try:
        entry_obj = None
        if entry is not None:
            entry_obj = markdown2.markdown(util.get_entry(entry))
            
        context = {
            "title": entry,
            "object": entry_obj,
        }
        return render(request, "encyclopedia/detail.django-html", context=context)
    except:
        context = {
            "title": entry,
        }
        return render(request, "encyclopedia/not_found.django-html", context=context)
    
def search(request):
    
    if request.method == 'POST':
        entries = util.list_entries()
        
        search_entry = request.POST.get("q")
        
        if search_entry in entries:
            return redirect("wiki_detail", entry=search_entry)
        
        similar_entries = [entry for entry in entries if search_entry in entry]
        
        if similar_entries:
            return render(request, "encyclopedia/search.django-html", {
                "search_entry": search_entry,
                "similar_entries": similar_entries,
            })
            
        return redirect("wiki_detail", entry=search_entry)
            
    if request.method == 'GET':
        return render(request, "encyclopedia/search_get.django-html")
            
        
def create_new_page(request):
    
    return render(request, "encyclopedia/create_new_page.django-html")

def handle_random(request):
    
    random_index = random.randint(0, len(util.list_entries())-1)
    
    return redirect("wiki_detail", entry=util.list_entries()[random_index])
    
    
    
    
    