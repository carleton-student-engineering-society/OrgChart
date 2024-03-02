# from django.shortcuts import render

from django.http import HttpResponse
from .models import Organization, Term, Role
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


def view_org_center(request, org: str, center: int):
    o = Organization.objects.filter(name=org).first()
    if o is None:
        return render(request, "view_org.html", {'error': True})
    nodes = []
    edges = []
    NODE_SHAPE = "box"
    if center == 0:
        terms = Term.objects.filter(end=None, role__org__name=org, role__manager=None)
    else:
        manager = Role.objects.filter(id=center).first()
        terms = Term.objects.filter(end=None, role__org__name=org, role__manager=manager)
        terms2 = Term.objects.filter(end=None, role=manager)
        above = Term.objects.filter(end=None, role=manager.manager)
        for term in terms2:
            start = term.start.strftime("%B %d, %Y")
            nodes += [{"id": term.role.id,
                       "label": term.role.name + " - " + term.person.name + " - " + start + " - " + term.role.email,
                       "shape": NODE_SHAPE}]
            if len(above) != 0:
                edges += [{"from": term.role.manager.id, "to": term.role.id, "arrows": "to"}]
        for term in above:
            nodes += [{"id": term.role.id, "label": term.role.name + " - " + term.person.name, "shape": NODE_SHAPE}]
    for term in terms:
        if center == 0:
            start = term.start.strftime("%B %d, %Y")
            nodes += [{"id": term.role.id,
                       "label": term.role.name + " - " + term.person.name + " - " + start + " - " + term.role.email,
                       "shape": NODE_SHAPE}]
        else:
            nodes += [{"id": term.role.id,
                       "label": term.role.name + " - " + term.person.name,
                       "shape": NODE_SHAPE}]
        terms2 = Term.objects.filter(end=None, role__org__name=org, role__manager=term.role)
        if center != 0:
            edges += [{"from": term.role.manager.id, "to": term.role.id, "arrows": "to"}]
        for term2 in terms2:
            nodes += [{"id": term2.role.id,
                       "label": term2.role.name + " - " + term2.person.name,
                       "shape": NODE_SHAPE}]
            edges += [{"from": term2.role.manager.id, "to": term2.role.id, "arrows": "to"}]
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
        return view_org_center(request, org, 0)
