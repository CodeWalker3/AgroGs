
from factory import Faker,SubFactory
from factory.django import DjangoModelFactory
from AgroGs.orders.models import Orders, PaymentMethod
from factory.fuzzy import FuzzyInteger, FuzzyDecimal

class PaymentMethodFactory(DjangoModelFactory):
    class Meta:
        model = PaymentMethod

    name = Faker('word')

class OrdersFactory(DjangoModelFactory):
    class Meta:
        model = Orders

    total = FuzzyDecimal(1,100)
    status = 'Em andamento'
    order_date = Faker('date_time_this_decade', before_now=True, after_now=False)
    payment = SubFactory(PaymentMethodFactory)
