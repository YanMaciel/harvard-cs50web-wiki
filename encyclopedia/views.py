from django.shortcuts import render
import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.django-html", {
        "entries": util.list_entries()
    })

def wiki_detail_view(request, entry=None):
    print(util.list_entries())
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
    
def search_entry_view(request, searched_entry=None):
    if searched_entry is not None:
        if searched_entry in util.list_entries():
            return wiki_detail_view(request, searched_entry)