import logging

from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.utils.encoding import force_str

from django_otp.models import SideChannelDevice, ThrottlingMixin
from django_otp.util import hex_validator, random_hex
import requests

from .conf import settings


logger = logging.getLogger(__name__)


def default_key():  # pragma: no cover
    """ Obsolete code here for migrations. """
    return force_str(random_hex(20))


def key_validator(value):  # pragma: no cover
    """ Obsolete code here for migrations. """
    return hex_validator(20)(value)


class CustomSMSDevice(ThrottlingMixin, SideChannelDevice):
    """
    A :class:`~django_otp.models.SideChannelDevice` that delivers a token via
    you Service Provider's SMS service.

    The tokens are valid for :setting:`OTP_SMS_TOKEN_VALIDITY` seconds. Once
    a token has been accepted, it is no longer valid.

    .. attribute:: number

        *CharField*: The mobile phone number to deliver to. It is recommended
        to use using the `E.164 <http://en.wikipedia.org/wiki/E.164>`_ format.
        For Zambian numbers, this would look like '+260970123456'.

    """
    number = models.CharField(
        max_length=30,
        help_text="The mobile number to deliver tokens to (E.164)."
    )

    class Meta(SideChannelDevice.Meta):
        verbose_name = "Custom SMS Device"

    def get_throttle_factor(self):
        return settings.OTP_SMS_THROTTLE_FACTOR

    def generate_challenge(self):
        """
        Sends the current TOTP token to ``self.number``.

        :returns: :setting:`OTP_SMS_CHALLENGE_MESSAGE` on success.
        :raises: Exception if delivery fails.

        """
        self.generate_token(valid_secs=settings.OTP_SMS_TOKEN_VALIDITY)

        message = settings.OTP_SMS_TOKEN_TEMPLATE.format(token=self.token)

        if settings.OTP_SMS_NO_DELIVERY:
            logger.info(message)
        else:
            self._deliver_token(message)

        challenge = settings.OTP_SMS_CHALLENGE_MESSAGE.format(token=self.token)

        return challenge

    def _deliver_token(self, token):
        self._validate_config()

        url = 'https://api.twilio.com/2010-04-01/Accounts/{0}/Messages.json'.format(settings.OTP_SMS_ACCOUNT)
        data = {
            'From': settings.OTP_SMS_FROM,
            'To': self.number,
            'Body': str(token),
        }

        response = requests.post(
            url, data=data,
            auth=(settings.OTP_SMS_ACCOUNT, settings.OTP_SMS_AUTH)
        )

        try:
            response.raise_for_status()
        except Exception as e:
            logger.exception('Error sending token by SMS: {0}'.format(e))
            raise

        if 'sid' not in response.json():
            message = response.json().get('message')
            logger.error('Error sending token by SMS: {0}'.format(message))
            raise Exception(message)

    def _validate_config(self):
        if settings.OTP_SMS_ACCOUNT is None:
            raise ImproperlyConfigured("OTP_SMS_ACCOUNT must be set to your Service Provider's account identifier")

        if settings.OTP_SMS_AUTH is None:
            raise ImproperlyConfigured("OTP_SMS_AUTH must be set to your Service Provider's auth token")

        if settings.OTP_SMS_FROM is None:
            raise ImproperlyConfigured('OTP_SMS_FROM must be set to one of your authorized phone numbers')

    def verify_token(self, token):
        verify_allowed, _ = self.verify_is_allowed()
        if verify_allowed:
            verified = super().verify_token(token)

            if verified:
                self.throttle_reset()
            else:
                self.throttle_increment()
        else:
            verified = False

        return verified
