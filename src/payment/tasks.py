from celery import task

from payment.models import Payment


@task
def capture_payment(pk):
    payment = Payment.objects.get(pk=pk)
    print(f"Capture payment: {payment}")
