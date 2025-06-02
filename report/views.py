from django.db.models import Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response

from location.models import Location
from product.models import Product
from product_movement.models import ProductMovement


@api_view(['GET'])
def product_balance_list(request):

    products = Product.objects.all()
    locations = Location.objects.all()

    product_balance = []

    for product in products:

        for location in locations:

            imported_qty = ProductMovement.objects.filter(
                product=product,
                to_location=location
            ).aggregate(total=Sum('qty'))

            # get the total exported quantity
            exported_qty = ProductMovement.objects.filter(
                product=product,
                from_location=location
            ).aggregate(total=Sum('qty'))

            count_imported_qty = imported_qty['total'] if imported_qty['total'] else 0
            count_exported_qty = exported_qty['total'] if exported_qty['total'] else 0

            balance = count_imported_qty - count_exported_qty

            if balance != 0:
                product_balance.append({
                    'product': product.name,
                    'warehouse': location.name,
                    'qty': balance
                })

    return Response(product_balance, status=200)