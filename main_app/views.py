from django.shortcuts import render

from settings_app.models import *
from .models import *
from more_app.models import OqituvchiKategoriyalari

# Create your views here.
def home_page(request):
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
    HOME_WELCOME = HomeWelcome.objects.last()
    HOME_YONALISHLAR = HomeYonalishlar.objects.last()
    HOME_YONALISHLAR_FOR = HomeYonalishlarDivs.objects.all()
    HOME_MAVJUD_YONALISHLAR = HomeMavjudYonalishlar.objects.all()
    HOME_ABOUT_ME = HomeAboutMe.objects.last()
    HOME_MEHNAT_FAOLIYATIM = HomeMehnatFaoliyatim.objects.last()
    HOME_MEHNAT_FAOLIYATIM_DIVS = HomeMehnatFaoliyatiDivs.objects.all()[:3]
    HOME_APP = HomeApp.objects.last()
    HOME_TELEGRAM_GROUP = HomeTelegramGroup.objects.last()
    HOME_QUESTION = HomeQuestion.objects.last()


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
        'HOME_WELCOME': HOME_WELCOME,
        'HOME_YONALISHLAR': HOME_YONALISHLAR,
        'HOME_YONALISHLAR_FOR': HOME_YONALISHLAR_FOR,
        'HOME_MAVJUD_YONALISHLAR': HOME_MAVJUD_YONALISHLAR,
        'HOME_ABOUT_ME': HOME_ABOUT_ME,
        'HOME_MEHNAT_FAOLIYATIM': HOME_MEHNAT_FAOLIYATIM,
        'HOME_MEHNAT_FAOLIYATIM_DIVS': HOME_MEHNAT_FAOLIYATIM_DIVS,
        'HOME_APP': HOME_APP,
        'HOME_TELEGRAM_GROUP': HOME_TELEGRAM_GROUP,
        'HOME_QUESTION': HOME_QUESTION,
    }
    return render(request, 'index.html', ctx)