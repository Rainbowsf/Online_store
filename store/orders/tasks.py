from celery import shared_task
from django.core.mail import send_mail
from .models import Order
from django.db import transaction

order__id = 0


@shared_task
def order_created(order_id):
    """
    Задача для отправки уведомления по электронной почте при успешном создании заказа.
    """
    order = Order.objects.get(id=order_id)
    global order__id
    order__id = order.id
    subject = 'Заказ номер {}'.format(order_id)
    message = '{},\n\nВы успешно создали заказ.\
                Номер вашего заказа {}.'.format(order.first_name, order.id)
    mail_sent = send_mail(subject,
                          message,
                          'fadeev200026@gmail.com',
                          [order.email])

    return mail_sent


transaction.on_commit(lambda: order_created.delay('1'))

