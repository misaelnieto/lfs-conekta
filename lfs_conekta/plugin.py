from lfs.plugins import PaymentMethodProcessor
from lfs.plugins import PM_ORDER_IMMEDIATELY
from lfs.plugins import PM_ORDER_ACCEPTED


class ConektaPaymentMethodProcessor(PaymentMethodProcessor):
    def process(self):
        total = self.order.price
        return {
            "accepted": True,
            "next_url": "http://www.acme.com/payment?id=4711&total=%s" % total,
        }

    def get_create_order_time(self):
        return PM_ORDER_IMMEDIATELY

    def get_pay_link(self):
        total = self.order.price
        return "http://www.acme.com/payment?id=4711&total=%s" % total
