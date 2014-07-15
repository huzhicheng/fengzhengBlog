#-*- coding:utf-8 -*-

from django.http import HttpResponse,Http404
import datetime
import os
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response



def hello(request,offset):
    try:
        offset = int(offset)
    except:
        raise Http404()

    #assert False
    response = HttpResponse("<input type='text' value='%s'/><span>%s</span>" % (datetime.datetime.now(),offset))
    return response

def test(request):
    return render_to_response("test.html",{"btnvalue":"我是动态标记内容，clicke me"})




def articlelist(request):
    template = get_template("ArticleList.html")
    html = template.render(Context({'pageTitle':'文章列表'}))
    return HttpResponse(html)


import MySQLdb

def book_list(request):
    db = MySQLdb.connect(user='huzhicheng', db='leak', passwd='517106011', host='localhost')
    cursor = db.cursor()
    cursor.execute('select username from users')
    names = [row[0] for row in cursor.fetchall()]
    db.close()
    #return render_to_response('list.html', {'names': names})
    return HttpResponse("<div>%s</div>" % names[0])
