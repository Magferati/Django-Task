from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import RepairOrder
from .services import reserve_stock

class CreateOrderAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        variant = request.data['variant_id']
        reserve_stock(variant)

        order = RepairOrder.objects.create(
            customer=request.user,
            vendor=variant.service.vendor,
            variant=variant,
            total_amount=variant.price
        )

        payment_url = f"https://fake-payment.com/pay/{order.order_id}"

        return Response({
            "order_id": order.order_id,
            "payment_url": payment_url
        })
