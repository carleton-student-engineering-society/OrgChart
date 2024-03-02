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
    NODE_SIZE = "100"
    if center == 0:
        terms = Term.objects.filter(end=None, role__org__name=org, role__manager=None)
    else:
        manager = Role.objects.filter(id=center).first()
        terms = Term.objects.filter(end=None, role__org__name=org, role__manager=manager)
        terms2 = Term.objects.filter(end=None, role=manager)
        if manager.manager is not None:
            above = Term.objects.filter(end=None, role=manager.manager)
        else:
            above = []
        names = ""
        for term in terms2:
            names += " - " + term.person.name
        start = term.start.strftime("%B %d, %Y")
        nodes += [{"id": term.role.id,
                   "label": term.role.name + names + " - " +
                  start + " - " + str(term.role.email),
                   "shape": NODE_SHAPE,
                   "size": NODE_SIZE,
                   "group": "current"}]
        if len(above) != 0:
            edges += [{"from": term.role.manager.id, "to": term.role.id, "arrows": "to"}]
        if len(above) > 0:
            names = ""
            for term in above:
                names += " - " + term.person.name
            term = above.first()
            nodes += [{"id": term.role.id,
                       "label": term.role.name + names,
                       "shape": NODE_SHAPE,
                       "size": NODE_SIZE,
                       "group": "above"}]
    for term in terms:
        found = False
        for node in nodes:
            if node['id'] == term.role.id:
                found = True
                break
        if found:
            continue
        t = Term.objects.filter(end=None, role=term.role)
        if len(t) > 1:
            names = ""
            for t1 in t:
                names += " - " + t1.person.name
        else:
            names = " - " + term.person.name
        if center == 0:
            start = term.start.strftime("%B %d, %Y")
            nodes += [{"id": term.role.id,
                       "label": term.role.name + names + " - " +
                       start + " - " + str(term.role.email),
                       "shape": NODE_SHAPE,
                       "size": NODE_SIZE,
                       "group": term.role.roletype}]
        else:
            nodes += [{"id": term.role.id,
                       "label": term.role.name + names,
                       "shape": NODE_SHAPE,
                       "size": NODE_SIZE,
                       "group": term.role.roletype}]
        if center != 0:
            edges += [{"from": term.role.manager.id, "to": term.role.id, "arrows": "to"}]
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
