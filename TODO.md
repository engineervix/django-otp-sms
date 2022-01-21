# TODO

Need to refactor the `_deliver_token` method in `otp_sms.models.CustomSMSDevice`.
Integrate with either of the following:

- [django-sendsms](https://github.com/stefanfoulis/django-sendsms)
- [django-sms](https://github.com/roaldnefs/django-sms#defining-a-custom-sms-backend)

Depending on which SMS API you choose, figure out how to deal with these **core settings** previously defined in [django-otp/django-otp-twilio](https://github.com/django-otp/django-otp-twilio/):

- **OTP_SMS_ACCOUNT** -- Your Custom SMS Service Provider account ID.  
- **OTP_SMS_AUTH**    -- Your Custom SMS Service Provider auth token.
- **OTP_SMS_FROM**    -- The phone number to send SMS messages from. This must be one of your numbers verified by your Service provider.

Whatever changes are made, the optional settings below will not be affected:

| Setting                   | Default Value | Description                                                                                                                                                                                                                                                        |
|---------------------------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OTP_SMS_CHALLENGE_MESSAGE | Sent by SMS   | The message returned by  `generate_challenge()` . This may contain '{token}', which will be replaced by the token. This completely negates any security benefit to the device, but it's handy for development, especially in combination with OTP_SMS_NO_DELIVERY. |
| OTP_SMS_NO_DELIVERY       | False         | Send tokens to the  `otp_sms.models`  logger instead of delivering them by SMS. Useful for development.                                                                                                                                                            |
| OTP_SMS_THROTTLE_FACTOR   | 1             | This controls the rate of throttling. The sequence of 1, 2, 4, 8… seconds is multiplied by this factor to define the delay imposed after 1, 2, 3, 4… successive failures. Set to 0 to disable throttling completely.                                               |
| OTP_SMS_TOKEN_TEMPLATE    | "{token}"     | A string template for generating the token message. By default, this is just the token itself, but you can customize it. The template will be rendered with Python string formatting (template.format(token=token)).                                               |
| OTP_SMS_TOKEN_VALIDITY    | 30            | The number of seconds for which a delivered token will be valid.                                                                                                                                                                                                   |
