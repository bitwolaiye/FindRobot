# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'WeiboUser.gender'
        db.add_column('Robot_weibouser', 'gender',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'WeiboUser.gender'
        db.delete_column('Robot_weibouser', 'gender')


    models = {
        'Robot.weibouser': {
            'Meta': {'object_name': 'WeiboUser'},
            'gender': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'small_avatar': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_desc': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['Robot']