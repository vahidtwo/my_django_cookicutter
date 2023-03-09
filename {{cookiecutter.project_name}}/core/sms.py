from django.conf import settings
from kavenegar import KavenegarAPI, APIException, HTTPException
import json


def send_sms():
    pass


def sms_character_replace(text):
    """
        replace space in text to send by kavenegar
    :param text: text
    :type text: str
    :return: replaced space text
    :rtype: str
    """
    return str(text).replace(" ", "‌").replace("_", "-").replace("_", "‌")  # kavenegar error 431


def send_sms_template(phone_number, template, **kwargs):
    api = KavenegarAPI(settings.KAVENEGAR_AUTH_TOKEN)
    for key, value in kwargs.items():
        if key.startswith("token"):
            kwargs[key] = sms_character_replace(value)

    params = {
        **kwargs,
        "receptor": phone_number,
        "template": template,
        "sender": settings.KAVENEGAR_SENDER_LINE,
    }
    try:
        response = api.verify_lookup(params)
        print(str(response))  # todo add logger
        return response
    except APIException as api_exception:
        print(str(api_exception))  # todo add logger
        return api_exception
    except HTTPException as http_exception:
        print(str(http_exception))  # todo add logger
        return http_exception
