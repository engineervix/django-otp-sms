django-otp-sms
=================

.. include:: ../../README.rst


Installation
------------

django-otp-sms can be installed via pip::

    pip install django-otp-sms


Once installed it should be added to INSTALLED_APPS after django_otp core::

    INSTALLED_APPS = [
        ...
        'django_otp',
        'django_otp.plugins.otp_totp',
        'django_otp.plugins.otp_hotp',
        'django_otp.plugins.otp_static',

        'otp_sms',
    ]


Custom SMS Devices
------------------

.. autoclass:: otp_sms.models.CustomSMSDevice
    :members:


Admin
-----

The following :class:`~django.contrib.admin.ModelAdmin` subclass is registered
with the default admin site. We recommend its use with custom admin sites as
well:

.. autoclass:: otp_sms.admin.CustomSMSDeviceAdmin


Settings
--------

.. setting:: OTP_SMS_ACCOUNT

**OTP_SMS_ACCOUNT**

Default: ``None``

Your Service Provider's account ID.


.. setting:: OTP_SMS_AUTH

**OTP_SMS_AUTH**

Default: ``None``

Your Service Provider's auth token.


.. setting:: OTP_SMS_CHALLENGE_MESSAGE

**OTP_SMS_CHALLENGE_MESSAGE**

Default: ``"Sent by SMS"``

The message returned by
:meth:`~otp_sms.models.CustomSMSDevice.generate_challenge`. This may contain
``'{token}'``, which will be replaced by the token. This completely negates any
security benefit to the device, but it's handy for development, especially in
combination with :setting:`OTP_SMS_NO_DELIVERY`.


.. setting:: OTP_SMS_FROM

**OTP_SMS_FROM**

Default: ``None``

The phone number to send SMS messages from. This must be one of your numbers authorized to send SMSes.


.. setting:: OTP_SMS_NO_DELIVERY

**OTP_SMS_NO_DELIVERY**

Default: ``False``

Send tokens to the 'otp_sms.models' logger instead of delivering them by SMS.
Useful for development.


.. setting:: OTP_SMS_THROTTLE_FACTOR

**OTP_SMS_THROTTLE_FACTOR**

Default: ``1``

This controls the rate of throttling. The sequence of 1, 2, 4, 8... seconds is
multiplied by this factor to define the delay imposed after 1, 2, 3, 4...
successive failures. Set to ``0`` to disable throttling completely.


.. setting:: OTP_SMS_TOKEN_TEMPLATE

**OTP_SMS_TOKEN_TEMPLATE**

Default: ``"{token}"``

A string template for generating the token message. By default, this is just the
token itself, but you can customize it. The template will be rendered with
Python string formatting (``template.format(token=token)``).


.. setting:: OTP_SMS_TOKEN_VALIDITY

**OTP_SMS_TOKEN_VALIDITY**

Default: ``30``

The number of seconds for which a delivered token will be valid.


Changes
-------

:doc:`changes`


License
-------

.. include:: ../../LICENSE
