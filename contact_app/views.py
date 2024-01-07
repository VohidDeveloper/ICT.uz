from django.shortcuts import render, redirect

# Telegram bot
import requests

from settings_app.models import *
from main_app.models import HomeMehnatFaoliyatiDivs, HomeMehnatFaoliyatim
from more_app.models import OqituvchiKategoriyalari

from .models import AboutMe, Message

def contact_page(request):
    TELEGRAM_BOT = TelegramBotSettings.objects.last()

    if request.method == "POST" and TELEGRAM_BOT:
        Message.objects.create(
            name=request.POST['name'],
            phone=request.POST['tg_username'],
            message=request.POST['message'],
        )

        url = f"https://api.telegram.org/bot{TELEGRAM_BOT.token}/sendMessage"

        payload = {
            "text": f"<b>✅ Yangi xabar:</b>\n\n"
                    f"<b>🧍‍♂️ Ism:</b> {request.POST['name']}\n"
                    f"<b>📬 Username:</b> {request.POST['tg_username']}\n"
                    f"<b>◽️ Xabar:</b> {request.POST['message']}",
            "chat_id": TELEGRAM_BOT.user_id,
            "parse_mode": "HTML",
        }
        headers = {
            "accept": "application/json",
            "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)",
            "content-type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)

        print(response.text)
        return redirect('home_page')

    # Required
    SEO_SETTINGS = SeoSettings.objects.last()
    FOOTER_SETTINGS = FooterSettings.objects.last()
    SOCIAL_SETTINGS = SocialSettings.objects.all()
    LOGO_SETTINGS = LogoSettings.objects.last()
    ONE_HEADER = OneHeader.objects.all()
    TWO_HEADER = TwoHeader.objects.all()
    RIGHT_BUTTON_SETTINGS = RightButtonSettings.objects.last()
    PHONE_EMAIL_SETTINGS = PhoneEmailSettings.objects.last()

    # Main
    ABOUT_ME = AboutMe.objects.last()

    ctx = {
        # Required
        'SEO_SETTINGS': SEO_SETTINGS,
        'FOOTER_SETTINGS': FOOTER_SETTINGS,
        'SOCIAL_SETTINGS': SOCIAL_SETTINGS,
        'LOGO_SETTINGS': LOGO_SETTINGS,
        'ONE_HEADER': ONE_HEADER,
        'TWO_HEADER': TWO_HEADER,
        'RIGHT_BUTTON_SETTINGS': RIGHT_BUTTON_SETTINGS,
        'PHONE_EMAIL_SETTINGS': PHONE_EMAIL_SETTINGS,

        # Main
        'ABOUT_ME': ABOUT_ME,

    }
    return render(request, 'contact.html', ctx)

def me_page(request):
    # Required
    SEO_SETTINGS = SeoSettings.objects.last()
    FOOTER_SETTINGS = FooterSettings.objects.last()
    SOCIAL_SETTINGS = SocialSettings.objects.all()
    LOGO_SETTINGS = LogoSettings.objects.last()
    ONE_HEADER = OneHeader.objects.all()
    TWO_HEADER = TwoHeader.objects.all()
    RIGHT_BUTTON_SETTINGS = RightButtonSettings.objects.last()
    PHONE_EMAIL_SETTINGS = PhoneEmailSettings.objects.last()

    barcha_kategoriyalar = OqituvchiKategoriyalari.objects.all()

    # Main
    ABOUT_ME = AboutMe.objects.last()
    MEHNAT_FAOLIYATI = HomeMehnatFaoliyatim.objects.last()
    MEHNAT_FAOLIYATI_DIVS = HomeMehnatFaoliyatiDivs.objects.all()

    ctx = {
        # Required
        'SEO_SETTINGS': SEO_SETTINGS,
        'FOOTER_SETTINGS': FOOTER_SETTINGS,
        'SOCIAL_SETTINGS': SOCIAL_SETTINGS,
        'LOGO_SETTINGS': LOGO_SETTINGS,
        'ONE_HEADER': ONE_HEADER,
        'TWO_HEADER': TWO_HEADER,
        'RIGHT_BUTTON_SETTINGS': RIGHT_BUTTON_SETTINGS,
        'PHONE_EMAIL_SETTINGS': PHONE_EMAIL_SETTINGS,

        'FAYLLAR_KATEGORIYASI': barcha_kategoriyalar,

        # Main
        'ABOUT_ME': ABOUT_ME,
        'MEHNAT_FAOLIYATI': MEHNAT_FAOLIYATI,
        'MEHNAT_FAOLIYATI_DIVS': MEHNAT_FAOLIYATI_DIVS,

    }
    return render(request, 'me.html', ctx)