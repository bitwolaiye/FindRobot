# encoding:utf8

from django.db import models
import webkit, gtk, jswebkit

# Create your models here.


class WeiboUser(models.Model):
    weibo_uid = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    small_avatar = models.CharField(max_length=100)
    user_desc = models.CharField(max_length=500, null=True)
    gender = models.PositiveSmallIntegerField(default=0)
    getcai_uid = models.BigIntegerField(null=True)
    selected = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = 'weibo_user'

    @classmethod
    def load(cls, i):
        result = '\n'.join(file('%d.html' % i).readlines())
        webview = webkit.WebView()
        webview.connect( 'load-finished', lambda v,f: gtk.main_quit() )
        webview.load_uri('file:///home/zhouqi/work/FindRobot/%d.html' % i)
        #webview.load_html_string(result,'')

        gtk.main()
        js = jswebkit.JSContext( webview.get_main_frame().get_global_context() )
        res = js.EvaluateScript('window.location.href')
        renderedBody = str( js.EvaluateScript( 'document.body.innerHTML' ) )

        f = open(str(i)+'_1.html', 'w')
        f.write(renderedBody)
        f.close()


class PicWeibo(models.Model):
    weibo_user = models.ForeignKey(WeiboUser)
    pic_url = models.CharField(max_length=200)
    weibo_text = models.CharField(max_length=500, null=True)
    selected = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = 'pic_weibo'


class PicAvatar(models.Model):
    weibo_user = models.ForeignKey(WeiboUser)
    pic_url = models.CharField(max_length=200)
    selected = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = 'pic_avatar'

