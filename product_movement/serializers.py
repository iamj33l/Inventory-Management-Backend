from django.db.models import Sum
from rest_framework import serializers

from .models import ProductMovement


class ProductMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMovement
        fields = '__all__'
        read_only_fields = ['timestamp']

    def validate(self, attrs):

        product = attrs.get('product')
        from_location = attrs.get('from_location')
        to_location = attrs.get('to_location')
        quantity = attrs.get('qty')

        if not from_location and not to_location:
            raise serializers.ValidationError("Either From or To location must be specified.")

        if from_location == to_location:
            raise serializers.ValidationError("From and To locations cannot be the same.")

        if from_location:

            imported_qty = ProductMovement.objects.filter(
                product=product,
                to_location=from_location
            ).aggregate(total=Sum('qty'))

            exported_qty = ProductMovement.objects.filter(
                product=product,
                from_location=from_location
            ).aggregate(total=Sum('qty'))

            count_imported_qty = imported_qty['total'] if imported_qty['total'] else 0
            count_exported_qty = exported_qty['total'] if exported_qty['total'] else 0

            available_qty = count_imported_qty - count_exported_qty

            print(available_qty)

            if available_qty < quantity:
                raise serializers.ValidationError(
                    f"Insufficient stock in {from_location.name}. Available: {available_qty}, Requested: {quantity}."
                )

        if to_location:

            imported_qty = ProductMovement.objects.filter(
                to_location=to_location
            ).aggregate(total=Sum('qty'))

            exported_qty = ProductMovement.objects.filter(
                from_location=to_location
            ).aggregate(total=Sum('qty'))

            count_imported_qty = imported_qty['total'] if imported_qty['total'] else 0
            count_exported_qty = exported_qty['total'] if exported_qty['total'] else 0

            available_qty = count_imported_qty - count_exported_qty

            if available_qty + quantity > to_location.capacity:
                raise serializers.ValidationError(
                    f"Exceeding capacity in {to_location.name}. Available: {available_qty}, Requested: {quantity}."
                )

        return attrs

class ProductMovementDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMovement
        fields = '__all__'
        read_only_fields = ['timestamp']
        depth = 1