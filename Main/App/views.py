from rest_framework.response import Response
from rest_framework.views import APIView
from .Serizalizer import *
from .models import *


def init():
    if Order.objects.count() == 0:
        p1 = Product.objects.create(name='Яблоко', description='description', price=200)
        p2 = Product.objects.create(name='Апельсин', description='description', price=300)

        order = Order.objects.create(total_price=p1.price + p2.price)

        order.products.add(p1)
        order.products.add(p2)


class OrderAPIView(APIView):

    def get(self, request):
        init()
        products = Order.objects.last().products.all()

        serializer = ProductSerializer(products, many=True).data

        return Response({"message": "это последняя корзина так как у нас нет user к которому ее можно подвязать",
                         'cart': {"id": Order.objects.last().id, 'products': serializer,
                                  'total_price': Order.objects.last().total_price}})

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'Order': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error': 'Method PUT not allowed'})

        try:
            instance = Order.objects.get(id=pk)
        except:
            return Response({'error': 'Object does not exit'})

        serializer = OrderSerializer(data=request.data, instance=instance)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'Order': serializer.data})

    def delete(self, request, *args, **kwargs):

        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error': 'Method DELETE not allowed'})

        try:
            order = Order.objects.last().products.get(id=pk)
        except:
            return Response({'error': 'Object does not exit'})

        name = order.name

        order.delete()

        return Response({'order': 'Delete product ' + name})
