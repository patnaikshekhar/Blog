# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Article.likes'
        db.add_column(u'blog_article', 'likes',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Comments.date'
        db.add_column(u'blog_comments', 'date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 5, 1, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Article.likes'
        db.delete_column(u'blog_article', 'likes')

        # Deleting field 'Comments.date'
        db.delete_column(u'blog_comments', 'date')


    models = {
        u'blog.article': {
            'Meta': {'object_name': 'Article'},
            'contents': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'blog.comments': {
            'Meta': {'object_name': 'Comments'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Article']"}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 5, 1, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['blog']