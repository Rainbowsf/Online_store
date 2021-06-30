from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    """
    Задача для отправки уведомления по электронной почте при успешном создании заказа.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Заказ номер {}.'.format(order_id)
    message = 'Добрый день, {},\n\nВы успешно создали заказ в нашем магазине.\n\n' \
              'Номер вашего заказа: {}.\n' \
              'В течение суток с вами свяжется оператор и уточнит детали доставки и оплаты.'.format(order.first_name, order.id)
    mail_sent = send_mail(subject,
                          message,
                          'fadeev200027@gmail.com',
                          [order.email])
    return mail_sent


@shared_task
def order_created_info(order_id):
    """
    Задача для отправки уведомления по электронной почте при успешном создании заказа.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Создан заказ номер {}.'.format(order_id)
    message = 'Номер закакза: {}.\n' \
              'Имя клиента: {} {}.\n' \
              'Телефон: {}.\n' \
              'Email: {}.\n' \
              'Город: {}.\n' \
              'Адресс: {}.\n' \
              'Почтовый Индекс: {}.'.format(order.id,
                                            order.first_name,
                                            order.last_name,
                                            order.phone,
                                            order.email,
                                            order.city,
                                            order.address,
                                            order.postal_code)

    info_mail_sent = send_mail(subject,
                               message,
                               'fadeev200027@gmail.com',
                               ['fadeev200025@gmail.com'])
    return info_mail_sent
