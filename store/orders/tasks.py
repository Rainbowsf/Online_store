from celery import shared_task
from django.core.mail import send_mail
from .models import Order, OrderItem


@shared_task
def order_created(order_id):
    """
    Задача для отправки уведомления по электронной почте при успешном создании заказа.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Заказ номер {}.'.format(order_id)
    message = 'Добрый день, {}!\n\nВы успешно создали заказ в нашем магазине.\n\n' \
              'Номер вашего заказа: {}.\n\n' \
              'Ваш заказ:\n\n'.format(order.first_name,
                                      order.id)
    prods = OrderItem.objects.filter(order=order)
    sum_price = 0
    el_num = 1
    for el in prods:
        sum_price += el.product.price
        message += 'Торвар {}: {}\n' \
                   'Цена: ₽{}\n\n'.format(el_num,
                                          el.product.name,
                                          el.product.price)
        el_num += 1
    message += 'В течение суток с вами свяжется оператор и уточнит детали доставки и оплаты.\n' \
               'С уважением, интеренет магазин N'
    mail_sent = send_mail(subject,
                          message,
                          'fadeev200027@gmail.com',
                          [order.email])
    return mail_sent


@shared_task
def order_created_info(order_id):
    """
    Задача для отправки уведомления по электронной почтеопреатору о созданном.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Создан заказ номер {}.'.format(order_id)
    message = 'Номер закакза: {}.\n' \
              'Имя клиента: {} {}.\n' \
              'Телефон: {}.\n' \
              'Email: {}.\n' \
              'Город: {}.\n' \
              'Адрес: {}.\n' \
              'Почтовый Индекс: {}.\n\nТовары:\n\n'.format(order.id,
                                                           order.first_name,
                                                           order.last_name,
                                                           order.phone,
                                                           order.email,
                                                           order.city,
                                                           order.address,
                                                           order.postal_code)
    prods = OrderItem.objects.filter(order=order)
    sum_price = 0
    el_num = 1
    for el in prods:
        sum_price += el.product.price
        message += 'Торвар {}:\n' \
                   'Название: {}\n' \
                   'id: {}\n' \
                   'Цена: ₽{}\n\n'.format(el_num,
                                          el.product.name,
                                          el.product.id,
                                          el.product.price)
        el_num += 1
    message += 'Сумма: ₽{}'.format(sum_price)
    info_mail_sent = send_mail(subject,
                               message,
                               'fadeev200027@gmail.com',
                               ['fadeev200025@gmail.com'])
    return info_mail_sent
