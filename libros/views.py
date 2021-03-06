# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from sqlalchemy.sql import select
from main.database import engine_libros
from .models import Categoria

def index(request):
	context = {'saludo': 'hola mundo'}
	return render(request, 'libros/index.html', context)

def rest(request):
	conn = engine_libros.connect()
	stmt = select([Categoria])
	return HttpResponse(json.dumps([dict(r) for r in conn.execute(stmt)]))