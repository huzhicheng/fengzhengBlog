#-*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url
import settings
from django.contrib import admin
import os
admin.autodiscover()

ROOT = os.path.dirname(__file__)

urlpatterns = patterns('',
    # Examples:
    url(r'^test$','fengzhengBlog.views.test'),
    url(r'^$', 'fengzhengBlog.blogapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r"^test/","fengzhengBlog.views.test",name="test"),
    url(r'^hello/(\d{1,2})/$',"fengzhengBlog.views.hello",name="hello"),
    url(r'^book_list/',"fengzhengBlog.views.book_list",name="book_list"),
    url(r'^adduser/','fengzhengBlog.blogapp.views.adduser',name='adduser'),
    url(r'^showusers/','fengzhengBlog.blogapp.views.showusers',name='showusers'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^article/(\d+)','fengzhengBlog.blogapp.views.articleView'),
    ( r'^css/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': ROOT+'/css' }
    ),
    ( r'^js/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': ROOT+'/js' }
    ),
    ( r'^images/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': ROOT+'/images' }
    ),
    ( r'^ueEditor/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': ROOT+'/ueEditor' }
    ),
)

urlpatterns+=patterns('',
    url(r'^fengzhengadmin','fengzhengBlog.admin.views.check_auth_redirect',{'template_name':'fengzhengadmin/index.html'}),
    url(r'^fengzhengusercheck','fengzhengBlog.admin.views.checkuser'),
    url(r'^fengzhenglogout','fengzhengBlog.admin.views.fengzhenglogout'),
    url(r'^typography','fengzhengBlog.admin.views.check_auth_redirect',{'template_name':'fengzhengadmin/typography.html'}),
    url(r'^wysiwyg','fengzhengBlog.admin.views.check_auth_redirect',{'template_name':'fengzhengadmin/wysiwyg.html'}),
    url(r'^gallery','fengzhengBlog.admin.views.check_auth_redirect',{'template_name':'fengzhengadmin/gallery.html'}), #图片 相册
    url(r'^master','fengzhengBlog.admin.views.check_auth_redirect',{'template_name':'fengzhengadmin/master.html'}), #基础页 母版页
    url(r'^error404','fengzhengBlog.admin.views.check_auth_redirect',{'template_name':'fengzhengadmin/error-404.html'}), #404错误页面
    url(r'^elements','fengzhengBlog.admin.views.check_auth_redirect',{'template_name':'fengzhengadmin/elements.html'}), #组件
    url(r'^buttons','fengzhengBlog.admin.views.check_auth_redirect',{'template_name':'fengzhengadmin/buttons.html'}), #按钮&图标
    url(r'^treeview','fengzhengBlog.admin.views.check_auth_redirect',{'template_name':'fengzhengadmin/treeview.html'}), #树菜单
    url(r'^jquery-ui','fengzhengBlog.admin.views.check_auth_redirect',{'template_name':'fengzhengadmin/jquery-ui.html'}), #Jquery ui
    url(r'^tables','fengzhengBlog.admin.views.check_auth_redirect',{'template_name':'fengzhengadmin/tables.html'}), #简单表格
    url(r'^jqgrid','fengzhengBlog.admin.views.check_auth_redirect',{'template_name':'fengzhengadmin/jqgrid.html'}), #jqgrid plugin
    url(r'^form-elements','fengzhengBlog.admin.views.check_auth_redirect',{'template_name':'fengzhengadmin/form-elements.html'}), #表单组件
    url(r'^form-wizard','fengzhengBlog.admin.views.check_auth_redirect',{'template_name':'fengzhengadmin/form-wizard.html'}), #表单提示验证
    url(r'^dropzone','fengzhengBlog.admin.views.check_auth_redirect',{'template_name':'fengzhengadmin/dropzone.html'}), #文件上传
    url(r'^widgets','fengzhengBlog.admin.views.check_auth_redirect',{'template_name':'fengzhengadmin/widgets.html'}), #插件
    url(r'^timeline','fengzhengBlog.admin.views.check_auth_redirect',{'template_name':'fengzhengadmin/timeline.html'}), #时间轴
    url(r'^profile','fengzhengBlog.admin.views.check_auth_redirect',{'template_name':'fengzhengadmin/profile.html'}), #个人信息
    url(r'^inbox','fengzhengBlog.admin.views.check_auth_redirect',{'template_name':'fengzhengadmin/inbox.html'}), #收件箱
    url(r'^pricing','fengzhengBlog.admin.views.check_auth_redirect',{'template_name':'fengzhengadmin/pricing.html'}), #售价单
    url(r'^error500','fengzhengBlog.admin.views.check_auth_redirect',{'template_name':'fengzhengadmin/error-500.html'}), #500错误页
    url(r'^grid','fengzhengBlog.admin.views.check_auth_redirect',{'template_name':'fengzhengadmin/grid.html'}), #网格布局
)

urlpatterns+=patterns('',
    url(r'^article-new','fengzhengBlog.admin.views.check_auth_redirect',{'template_name':'fengzhengadmin/ArticleManage/ArticleNew.html'}),
    url(r'^article-post','fengzhengBlog.blogapp.views.saveArticle'),
    url(r'^getCategory$','fengzhengBlog.blogapp.views.asynHandler',{'action':'getCategory'}),#获取分类
    url(r'^getCategoryfortable','fengzhengBlog.blogapp.views.asynHandler',{'action':'getCategoryfortable'}),#获取分类
    url(r'^saveClassic','fengzhengBlog.blogapp.views.asynHandler',{'action':'saveClassic'}),#保存分类
    url(r'^updateClassic','fengzhengBlog.blogapp.views.asynHandler',{'action':'updateClassic'}),
    url(r'^deleteCategory$','fengzhengBlog.blogapp.views.asynHandler',{'action':'deleteCategory'}),#获取分类
    url(r'^articlelist','fengzhengBlog.blogapp.views.getList'),
    url(r'^article-edit/(\d+)','fengzhengBlog.blogapp.views.editArticle'),#文章编辑页面 (\d+)为文章id
    url(r'^delete-Article','fengzhengBlog.blogapp.views.asynHandler',{'action':'deleteArticle'}),
    url(r'^classic','fengzhengBlog.admin.views.check_auth_redirect',{'template_name':'fengzhengadmin/ClassicManage/classicNew.html'}),
    url(r'^comment-commit$','fengzhengBlog.blogapp.views.asynHandler',{'action':'commitComment'}),#提交评论
)


urlpatterns+=patterns('',
    url(r'^ueEditorControler','fengzhengBlog.admin.controller.handler'),
)