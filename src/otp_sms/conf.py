import django.conf
import django.test.utils


class Settings(object):
    """
    This is a simple class to take the place of the global settings object. An
    instance will contain all of our settings as attributes, with default
    values if they are not specified by the configuration.
    """
    _defaults = {
        'OTP_SMS_ACCOUNT': None,
        'OTP_SMS_AUTH': None,
        'OTP_SMS_CHALLENGE_MESSAGE': "Sent by SMS",
        'OTP_SMS_FROM': None,
        'OTP_SMS_NO_DELIVERY': False,
        'OTP_SMS_THROTTLE_FACTOR': 1,
        'OTP_SMS_TOKEN_TEMPLATE': '{token}',
        'OTP_SMS_TOKEN_VALIDITY': 30,
    }

    def __getattr__(self, name):
        if hasattr(django.conf.settings, name):
            value = getattr(django.conf.settings, name)
        elif name in self._defaults:
            value = self._defaults[name]
        else:
            raise AttributeError(name)

        return value


settings = Settings()
