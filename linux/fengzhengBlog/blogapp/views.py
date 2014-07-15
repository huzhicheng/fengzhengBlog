#-*- coding:utf-8 -*-

from django.shortcuts import render_to_response,render
from fengzhengBlog.blogapp.models import *
import datetime
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import Http404
import logging

def adduser(request):
    u = fz_user(1,u'风筝','fengzheng','mima','fengzheng@126.com',True,datetime.datetime.today())
    result = u.save()
    return HttpResponse(u"<div>添加成功%s</div>" % result)

def showusers(request):
    ulist = fz_user.objects.all()

    return HttpResponse( request.GET['q'])


#首页 加载文章列表 和 分类信息
#articles=fz_Article.objects.extra(where=["ispublished=1"])
def home(request):
    cate = request.GET.get("cate")
    c = None
    if cate:
    	c = fz_classic.objects.get(id=int(cate))

    classics = fz_classic.objects.all()
    articles=cate==None and fz_Article.objects.filter(ispublished=1) or fz_Article.objects.filter(ispublished=1).filter(classic=c)
    return render_to_response('index.html',{'articles':articles,'classes':classics})

#文章查看
def articleView(request,post_id):
	classics = fz_classic.objects.all()

	if post_id and post_id!="":
		article = fz_Article.objects.get(id=post_id)
		article.readcount+=1
		article.save()

	comments = fz_comment.objects.filter(article=article)
	return render_to_response("article.html",{"article":article,'classes':classics,"comments":comments})

#获取所有分类
def getCategory(request):
	categories = fz_classic.objects.all()
	#以下代码将一个集合对象转换成json字符串
	catearry = []
	for category in categories:
		catearry.append('{"id":%s,"name":"%s","articecount":%s}' % (category.id,category.name,category.articecount))
	result="["+",".join(catearry)+"]"	
	return HttpResponse(result)

def getCategoryfortable(request):
	categories = fz_classic.objects.all()
	#以下代码将一个集合对象转换成json字符串
	catearry = []
	for category in categories:
		catearry.append(u'''[{0},"<a data-id='{0}' href='javascript:EditClassic({0})'>{1}</a>",{2},"@action@"]'''.format(category.id,category.name,category.articecount))
	result="["+",".join(catearry)+"]"	
	return HttpResponse(result)

#保存分类
def saveClassic(request):
	if request.POST:
		classicName = request.POST.get("name")
		m= fz_classic.objects.filter(name=classicName)
		if m:
			return HttpResponse("分类已存在")

		p=fz_classic(name=classicName,articecount=0)
		p.save()
	return HttpResponse("ok")

#编辑更新分类
def updateClassic(request):
	if request.POST:
		classicName = request.POST.get("name")
		cid = request.POST.get("id")
		m= fz_classic.objects.get(id=cid)
		if m:
			m.name = classicName
			m.save()
		else:
			return HttpResponse("更新异常")
	return HttpResponse("ok")
	

#删除分类	  
def deleteCategory(request):
	if request.method=="POST":
		try:
			id = request.POST.get("id")
			if id and id !='':
				classic = fz_classic.objects.get(id=id)
				if classic:
					classic.delete()
		except Excpet,e:return HttpResponse(e)
	else:pass

	return HttpResponse("ok")


def deleteArticle(request):
	try:
		if request.POST:
			ids = request.POST.get("ids")
			removeRecords = fz_Article.objects.extra(where=["id in ("+ids + ")"])
			removeRecords.delete()
	except:
		return HttpResponse("删除失败")
	return HttpResponse("ok")

#提交评论
def commitComment(request):
	try:
		if request.POST:
			nickname = request.POST.get("nickname")
			email = request.POST.get("email")
			commentContent = request.POST.get("content")
			articleId = request.POST.get("articleId")
			article=fz_Article.objects.get(id=int(articleId))
			commentdate = datetime.datetime.now()
			comment = fz_comment(article=article,comment_content=commentContent,comment_date=commentdate,email=email,commentator=nickname)
			comment.save()

			article.commentcount+=1
			article.save()
	except:
		return HttpResponse("")
	return HttpResponse("ok")



#定义异步操作类型
actions = {
	"getCategory":getCategory,
	"deleteArticle":deleteArticle,
	"getCategoryfortable":getCategoryfortable,
	"saveClassic":saveClassic,
	"deleteCategory":deleteCategory,
	"updateClassic":updateClassic,
	"commitComment":commitComment
} 


#统一异步处理接口
@csrf_exempt
def asynHandler(request,action):
	return actions.get(action)(request)

#表单提交 必须添加@csrf_exempt装饰器
@csrf_exempt
def saveArticle(request):
	if request.method=="POST":
		isUpdate = request.POST.get("post_id") and True or False
		isFirstSave = not isUpdate

		title = request.POST.get("title")
		content = request.POST.get("content")
		ispublish = request.POST.get("form-field-radio")
		categoryId = request.POST.get("category_id_hidden")
		tags = request.POST.get("tags")
		publishDate = datetime.datetime.now()
		author=fz_user.objects.get(id=1)
		classic=fz_classic.objects.get(id=categoryId)
		if request.POST.get("post_id"):
			article=fz_Article.objects.get(id=request.POST.get("post_id"))
			article.title = title
			article.content = content
			article.ispublished = bool(int(ispublish))
			article.tags=tags
			article.classic = classic
		else:
			article = fz_Article(title=title,content=content,author=author,classic=classic,publish_date=publishDate,ispublished=bool(int(ispublish)),commentcount=0,readcount=0,tags=tags)
		article.save()
		return render_to_response("fengzhengadmin/ArticleManage/ArticleEdit.html",{"article":article,"isSave":isFirstSave,"isEdit":False,"isUpdate":isUpdate})
	else:
		return render_to_response("index.html")

def editArticle(request,post_id):
	#raise Http404(post_id)
	article = fz_Article.objects.get(id=post_id)
	if article:
		return render_to_response("fengzhengadmin/ArticleManage/ArticleEdit.html",{"article":article,"isSave":False,"isEdit":True,"isUpdate":False})
	else:
		return render_to_response("fengzhengadmin/error-404.html")



#获取文章列表
def getList(request):
	if request.user.is_authenticated():
		artlist = fz_Article.objects.all() 
		return render_to_response("fengzhengadmin/ArticleManage/ArticleList.html",{"list":artlist,"currentUser":request.user.first_name+request.user.last_name})
	else:
		return render_to_response("fengzhengadmin/login.html")
