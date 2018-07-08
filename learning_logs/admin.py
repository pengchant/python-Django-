from django.contrib import admin

from learning_logs.models import Topic, Entry

# 向admin注册模型
admin.site.register(Topic)
admin.site.register(Entry)