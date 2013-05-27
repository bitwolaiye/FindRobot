# encoding:utf8

from django.db import models
# import webkit, gtk, jswebkit

# Create your models here.

from weibo import APIClient

APP_KEY = '2534587164'            # app key
APP_SECRET = '1a2545c30de6165611736a6ec0961bf7'      # app secret
APP_ACCESS_TOKEN = '2.00jObfECIurWlC0e2627358fH1DWGD'
CALLBACK_URL = 'http://about.me'

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
    def test(cls):
        client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
        url = client.get_authorize_url()
        r = client.statuses.user_timeline.get(uid=1062004271, source=APP_KEY, access_token=APP_ACCESS_TOKEN, page=2)
        for st in r.statuses:
            if st.has_key('original_pic'):
                print st.text
                print st.original_pic


    # @classmethod
    # def load(cls, i):
    #     result = '\n'.join(file('%d.html' % i).readlines())
    #     webview = webkit.WebView()
    #     webview.connect( 'load-finished', lambda v,f: gtk.main_quit() )
    #     webview.load_uri('file:///home/zhouqi/work/FindRobot/%d.html' % i)
    #     #webview.load_html_string(result,'')
    #
    #     gtk.main()
    #     js = jswebkit.JSContext( webview.get_main_frame().get_global_context() )
    #     res = js.EvaluateScript('window.location.href')
    #     renderedBody = str( js.EvaluateScript( 'document.body.innerHTML' ) )
    #
    #     f = open(str(i)+'_1.html', 'w')
    #     f.write(renderedBody)
    #     f.close()


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

