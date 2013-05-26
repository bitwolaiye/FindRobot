# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WeiboUser'
        db.create_table('Robot_weibouser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('small_avatar', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('user_desc', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('Robot', ['WeiboUser'])


    def backwards(self, orm):
        # Deleting model 'WeiboUser'
        db.delete_table('Robot_weibouser')


    models = {
        'Robot.weibouser': {
            'Meta': {'object_name': 'WeiboUser'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'small_avatar': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_desc': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['Robot']