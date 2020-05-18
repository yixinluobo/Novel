from rest_framework import serializers
from novel import models


class ChapterModelSerializers(serializers.ModelSerializer):
    contents = serializers.SerializerMethodField(label='内容')

    class Meta:
        model = models.Chapter
        fields = ['id', 'title', 'create_time', 'contents']

    def get_contents(self, obj):
        with open(obj.content.path, 'r', encoding='utf8') as rf:
            contents = rf.read()

        # 对内容进行简单加密
        result = ''
        for i in contents:
            result += str(ord(i)) + 'l'
        return result


class NovelModelSerializer(serializers.ModelSerializer):
    chapters = ChapterModelSerializers(many=True)
    status = serializers.SerializerMethodField(label='状态')
    brand = serializers.SerializerMethodField(label='类型')

    class Meta:
        model = models.Novel
        fields = ['id', 'name', 'author', 'icon', 'views', 'brand', 'status', 'chapters']
        # fields = "__all__"

    def get_status(self, obj):
        status_num = obj.status
        if status_num == 0:
            return '连载中'
        return '已完结'

    def get_brand(self, obj):
        name = obj.brand.name
        return name


# 小说分类
class BrandModelSerializer(serializers.ModelSerializer):
    novels = NovelModelSerializer(many=True)

    class Meta:
        model = models.Brand
        fields = ['id', 'name', 'novels']
