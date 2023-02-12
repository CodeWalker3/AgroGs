
from factory import Faker,SubFactory
from factory.django import DjangoModelFactory
from AgroGs.orders.models import Orders, ProductOrder
from factory.fuzzy import FuzzyInteger, FuzzyDecimal
from AgroGs.products.tests.test_base import ProductFactory
from AgroGs.users.tests.test_base import UserFactory

class OrdersFactory(DjangoModelFactory):
    class Meta:
        model = Orders
    user = SubFactory(UserFactory)
    total = FuzzyDecimal(1,100)
    status = 'Em andamento'
    order_date = Faker('date_time_this_decade', before_now=True, after_now=False)

class OrdersFactory(DjangoModelFactory):
    class Meta:
        model = Orders

    total = Faker('pydecimal', left_digits=5, right_digits=2, positive=True)
    status = Faker('random_element', elements=Orders.ChoiceStatus)
    order_date = Faker('date_time_this_decade')
    update_date = Faker('date_time_this_decade')
    user = SubFactory(UserFactory)

class ProductOrderFactory(DjangoModelFactory):
    class Meta:
        model = ProductOrder

    product = SubFactory(ProductFactory)
    order = SubFactory(OrdersFactory)
    quantity = Faker('random_digit')
    
