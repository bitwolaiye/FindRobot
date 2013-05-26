# Scrapy settings for Scrapy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'Scrapy'

SPIDER_MODULES = ['Scrapy.spiders']
NEWSPIDER_MODULE = 'Scrapy.spiders'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware': None,
    # 'Scrapy.WebkitDownloader.WebkitDownloader': 543,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Scrapy (+http://www.yourdomain.com)'

def setup_django_env(path):
    import imp, os
    from django.core.management import setup_environ

    f, filename, desc = imp.find_module('settings', [path])
    project = imp.load_module('settings', f, filename, desc)

    setup_environ(project)

setup_django_env('/home/zhouqi/work/FindRobot/FindRobot/')

#which spider should use WEBKIT
WEBKIT_DOWNLOADER=['ccb']


import os
os.environ["DISPLAY"] = ":0"