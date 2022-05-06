from celery import shared_task

from payment.models import Payment


@shared_task
def capture_payment(pk):
    payment = Payment.objects.get(pk=pk)
    print(f"Capture payment: {payment}")
