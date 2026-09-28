from decimal import Decimal
from django.conf import settings
from shop.models import Product, Size


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    @staticmethod
    def _generate_item_key(product_id, size_id):
        return f"{product_id}_{size_id}" if size_id else str(product_id)

    def add(self, product, quantity=1, size_id=None, update_quantity=False):
        item_key = self._generate_item_key(product.id, size_id)
        if item_key not in self.cart:
            self.cart[item_key] = {
                'product_id': str(product.id),
                'quantity': 0,
                'price': str(product.price),
                'size_id': size_id
            }
        if update_quantity:
            self.cart[item_key]['quantity'] = quantity
        else:
            self.cart[item_key]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product_id, size_id=None):
        item_key = self._generate_item_key(product_id, size_id)
        if item_key in self.cart:
            del self.cart[item_key]
            self.save()

    def __iter__(self):
        cart_copy = {key: value.copy() for key, value in self.cart.items()}

        product_ids = {item['product_id'] for item in cart_copy.values()}
        products_map = {str(p.id): p for p in Product.objects.filter(id__in=product_ids)}

        size_ids = {item['size_id'] for item in cart_copy.values() if item['size_id']}
        sizes_map = {s.id: s.size for s in Size.objects.filter(id__in=size_ids)}

        for item_key, item in cart_copy.items():
            product = products_map.get(item['product_id'])
            if not product:
                continue

            item['product'] = product
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            item['size'] = sizes_map.get(item['size_id']) if item['size_id'] else None

            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        if settings.CART_SESSION_ID in self.session:
            del self.session[settings.CART_SESSION_ID]
            self.save()