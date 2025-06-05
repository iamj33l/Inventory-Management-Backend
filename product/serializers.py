from rest_framework import serializers

from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):

    category = serializers.CharField()

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        category_name = validated_data.pop('category')
        category, is_created = Category.objects.get_or_create(name=category_name)
        validated_data['category'] = category
        return super().create(validated_data)

    def update(self, instance, validated_data):
        category_name = validated_data.pop('category')
        if category_name:
            category, is_created = Category.objects.get_or_create(name=category_name)
            instance.category = category
        return super().update(instance, validated_data)
