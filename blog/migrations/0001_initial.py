# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table(u'blog_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('contents', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'blog', ['Article'])

        # Adding model 'Comments'
        db.create_table(u'blog_comments', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Article'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'blog', ['Comments'])


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table(u'blog_article')

        # Deleting model 'Comments'
        db.delete_table(u'blog_comments')


    models = {
        u'blog.article': {
            'Meta': {'object_name': 'Article'},
            'contents': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'blog.comments': {
            'Meta': {'object_name': 'Comments'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Article']"}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['blog']