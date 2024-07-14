from rest_framework import serializers

from trading_network.models import Contacts, Product, Element


class ContactSerializer(serializers.ModelSerializer):
    """
    Класс-сериализатор для модели Contacts.
    """

    class Meta:
        model = Contacts
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """
    Класс-сериализатор для модели Product.
    """

    class Meta:
        model = Product
        fields = '__all__'


class ElementSerializer(serializers.ModelSerializer):
    """
    Класс-сериализатор для модели Element.
    """

    contacts = ContactSerializer(many=True, read_only=True, required=False)
    products = ProductSerializer(many=True, read_only=True, required=False)
    supplier = serializers.SlugRelatedField(required=False, queryset=Element.objects.all(), slug_field="title")

    class Meta:
        model = Element
        fields = '__all__'
