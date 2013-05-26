# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WeiboUser'
        db.create_table('weibo_user', (
            ('weibo_uid', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('small_avatar', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('user_desc', self.gf('django.db.models.fields.CharField')(max_length=500, null=True)),
            ('gender', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('getcai_uid', self.gf('django.db.models.fields.BigIntegerField')(null=True)),
        ))
        db.send_create_signal('Robot', ['WeiboUser'])

        # Adding model 'PicWeibo'
        db.create_table('pic_weibo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('weibo_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Robot.WeiboUser'])),
            ('pic_url', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('weibo_text', self.gf('django.db.models.fields.CharField')(max_length=500, null=True)),
            ('selected', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal('Robot', ['PicWeibo'])

        # Adding model 'PicAvatar'
        db.create_table('pic_avatar', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('weibo_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Robot.WeiboUser'])),
            ('pic_url', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('selected', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal('Robot', ['PicAvatar'])


    def backwards(self, orm):
        # Deleting model 'WeiboUser'
        db.delete_table('weibo_user')

        # Deleting model 'PicWeibo'
        db.delete_table('pic_weibo')

        # Deleting model 'PicAvatar'
        db.delete_table('pic_avatar')


    models = {
        'Robot.picavatar': {
            'Meta': {'object_name': 'PicAvatar', 'db_table': "'pic_avatar'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pic_url': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'selected': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'weibo_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Robot.WeiboUser']"})
        },
        'Robot.picweibo': {
            'Meta': {'object_name': 'PicWeibo', 'db_table': "'pic_weibo'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pic_url': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'selected': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'weibo_text': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'weibo_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Robot.WeiboUser']"})
        },
        'Robot.weibouser': {
            'Meta': {'object_name': 'WeiboUser', 'db_table': "'weibo_user'"},
            'gender': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'getcai_uid': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'small_avatar': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_desc': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'weibo_uid': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['Robot']