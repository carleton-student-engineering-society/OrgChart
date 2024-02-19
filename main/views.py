# from django.shortcuts import render

from django.http import HttpResponse
from .models import Organization, Term
from django.shortcuts import render  # noqa F401
from django.contrib.admin.views.decorators import staff_member_required
import json


def index(request):
    return HttpResponse("Hello, world. You're at the index.")


def search(request):
    pass


def search_pattern(request, pattern: str):
    pass


def view(request):
    pass


def view_role(request, id: int):
    pass


def view_org(request, org: str):
    o = Organization.objects.filter(name=org).first()
    if o is None:
        return render(request, "view_org.html", {'error': True})
    terms = Term.objects.filter(end=None).filter(role__org__name=org)
    nodes = []
    edges = []
    done = {}
    for term in terms:
        if not done.get(term.role.id, False):
            nodes += [{"id": term.role.id, "label": term.role.name + " - " + term.person.name}]
            done[term.role.id] = True
            if term.role.manager is not None:
                edges += [{"from": term.role.manager.id, "to": term.role.id, "arrows": "to"}]
        else:
            id = term.role.id
            for i in range(len(nodes)):
                node = nodes[i]
                if node['id'] == id:
                    node['label'] += " - " + term.person.name
                    nodes[i] = node
                    break
    return render(request, "view_org.html", {'org': o, 'nodes': json.dumps(nodes), 'edges': json.dumps(edges)})


def add(request, org: str):
    pass


@staff_member_required
def create_org(request):
    if request.method == "GET":
        return render(request, "create_org.html", {'error': False})
    elif request.method == "POST":
        org = request.POST.get('org', None)
        if org is None:
            return render(request, "create_org.html", {'error': True})
        o = Organization.objects.filter(name=org).first()
        if o is not None:
            return render(request, "create_org.html", {'error': True})
        o = Organization(name=org)
        o.save()
        return view_org(request, org)
