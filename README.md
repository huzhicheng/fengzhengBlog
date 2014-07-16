> 本项目使用django实现了一个简易blog系统，功能非常有限，只有简单的文章和分类的管理及用户登录验证功能，权限、角色之类的功能暂时没有。

这里提供了windows和linux两个版本，分别在windows和linux文件夹下。

启动网站，预览效果：
windows版：
可进入windows文件夹，执行python manage.py runserver port
或者直接运行runserver1989.cmd 直接在1989端口下预览效果。

linux版：
可进入linux文件夹，执行python manage.py runserver port
或者直接运行runserver1989.sh  直接在1989端口下预览效果。

首页地址：http://127.0.0.1:port
后台管理页面地址：http://127.0.0.1/fengzhengadmin

进入管理页面后，输入的用户名和密码需要是执行数据模型同步时创建的用户，或者用超级管理员访问django自己的后台登录页面（http://127.0.0.1:port/admin）后添加的用户。
