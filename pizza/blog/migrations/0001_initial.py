# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FileFormat'
        db.create_table('blog_fileformat', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ext', self.gf('django.db.models.fields.SlugField')(max_length=10)),
        ))
        db.send_create_signal('blog', ['FileFormat'])

        # Adding model 'Blog'
        db.create_table('blog_blog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('podcast', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('blog', ['Blog'])

        # Adding M2M table for field authors on 'Blog'
        m2m_table_name = db.shorten_name('blog_blog_authors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('blog', models.ForeignKey(orm['blog.blog'], null=False)),
            ('author', models.ForeignKey(orm['kitchen_sink.author'], null=False))
        ))
        db.create_unique(m2m_table_name, ['blog_id', 'author_id'])

        # Adding M2M table for field sites on 'Blog'
        m2m_table_name = db.shorten_name('blog_blog_sites')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('blog', models.ForeignKey(orm['blog.blog'], null=False)),
            ('site', models.ForeignKey(orm['sites.site'], null=False))
        ))
        db.create_unique(m2m_table_name, ['blog_id', 'site_id'])

        # Adding model 'Category'
        db.create_table('blog_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=200)),
        ))
        db.send_create_signal('blog', ['Category'])

        # Adding model 'Post'
        db.create_table('blog_post', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('blog', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Blog'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=200)),
            ('publish', self.gf('django.db.models.fields.DateTimeField')()),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['kitchen_sink.Image'], null=True, blank=True)),
            ('imageset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['kitchen_sink.ImageSet'], null=True, blank=True)),
        ))
        db.send_create_signal('blog', ['Post'])

        # Adding M2M table for field authors on 'Post'
        m2m_table_name = db.shorten_name('blog_post_authors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm['blog.post'], null=False)),
            ('author', models.ForeignKey(orm['kitchen_sink.author'], null=False))
        ))
        db.create_unique(m2m_table_name, ['post_id', 'author_id'])

        # Adding M2M table for field categories on 'Post'
        m2m_table_name = db.shorten_name('blog_post_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm['blog.post'], null=False)),
            ('category', models.ForeignKey(orm['blog.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['post_id', 'category_id'])

        # Adding model 'MediaFile'
        db.create_table('blog_mediafile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('ext', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.FileFormat'])),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Post'])),
        ))
        db.send_create_signal('blog', ['MediaFile'])


    def backwards(self, orm):
        # Deleting model 'FileFormat'
        db.delete_table('blog_fileformat')

        # Deleting model 'Blog'
        db.delete_table('blog_blog')

        # Removing M2M table for field authors on 'Blog'
        db.delete_table(db.shorten_name('blog_blog_authors'))

        # Removing M2M table for field sites on 'Blog'
        db.delete_table(db.shorten_name('blog_blog_sites'))

        # Deleting model 'Category'
        db.delete_table('blog_category')

        # Deleting model 'Post'
        db.delete_table('blog_post')

        # Removing M2M table for field authors on 'Post'
        db.delete_table(db.shorten_name('blog_post_authors'))

        # Removing M2M table for field categories on 'Post'
        db.delete_table(db.shorten_name('blog_post_categories'))

        # Deleting model 'MediaFile'
        db.delete_table('blog_mediafile')


    models = {
        'blog.blog': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Blog'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['kitchen_sink.Author']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'podcast': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['sites.Site']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'blog.category': {
            'Meta': {'ordering': "('slug',)", 'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'blog.fileformat': {
            'Meta': {'ordering': "('title',)", 'object_name': 'FileFormat'},
            'ext': ('django.db.models.fields.SlugField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'blog.mediafile': {
            'Meta': {'object_name': 'MediaFile'},
            'ext': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.FileFormat']"}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Post']"})
        },
        'blog.post': {
            'Meta': {'ordering': "('-publish',)", 'object_name': 'Post'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['kitchen_sink.Author']", 'null': 'True', 'blank': 'True'}),
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Blog']"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['blog.Category']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['kitchen_sink.Image']", 'null': 'True', 'blank': 'True'}),
            'imageset': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['kitchen_sink.ImageSet']", 'null': 'True', 'blank': 'True'}),
            'publish': ('django.db.models.fields.DateTimeField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'kitchen_sink.author': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Author'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['kitchen_sink.Image']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['sites.Site']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'})
        },
        'kitchen_sink.image': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Image'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'caption_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'credit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'credit_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'kitchen_sink.imageset': {
            'Meta': {'ordering': "('title',)", 'object_name': 'ImageSet'},
            'captype': ('django.db.models.fields.CharField', [], {'default': "'override'", 'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['blog']