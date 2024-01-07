import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-x=ha&6zv-%&z93l^7=#!evow&4i3cttx)9cvre_&=mduo_n-s6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
# ALLOWED_HOSTS = ['ict-for-students.uz', 'www.ict-for-students.uz', '167.71.49.146', 'localhost']

# Application definition

INSTALLED_APPS = [
    # Admin NEW UI
    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local APPS
    'settings_app',
    'main_app',
    'course_app',
    'contact_app',
    'more_app',
    'quiz_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ICT.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ICT.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'ict_db',
#         'USER': 'ict_user',
#         'PASSWORD': 'Bo^725726lyKGerYJ',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'uz'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
# STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DATA_UPLOAD_MAX_MEMORY_SIZE = 524288333

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# JAZZMIN SETTINGS
JAZZMIN_SETTINGS = {
    "site_title": "ICT-FOR-STUDENTS.UZ | Superadminstrator",

    "site_header": "ICT-FOR-STUDENTS",

    "site_brand": "ICT-FOR-STUDENTS",

    "site_logo": "custom/logo.png",

    "login_logo": "custom/new-logo.png",

    "login_logo_dark": "custom/new-logo.png",

    "site_logo_classes": "",

    "site_icon": None,

    "welcome_sign": "ICT-FOR-STUDENTS Admin paneliga xush kelibsiz!",

    "copyright": "ICT-FOR-STUDENTS",

    "search_model": [],

    "user_avatar": None,

    # Links to put along the top menu
    "topmenu_links": [
        {
            "name": "Bosh sahifa",
            "url": "admin:index",
            "permissions": ["auth.view_user"]
        },
    ],

    "usermenu_links": [
    ],

    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": True,

    "hide_apps": [],

    "hide_models": [],

    "order_with_respect_to": [],

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",

        "news_app.news": "fas fa-newspaper",
        "news_app.category": "fas fa-tools",

        "page_app.page": "fas fa-tv",

        "components_app.oneheader": "nav-icon fa fa-bolt",
        "components_app.twoheader": "nav-icon fa fa-gamepad",
        "components_app.threeheader": "nav-icon fa fa-hashtag",

        "components_app.seosettings": "nav-icon fa fa-wrench",
        "components_app.topheader": "nav-icon fa fa-window-maximize",
        "components_app.headerlogo": "nav-icon fa fa-power-off",
        "components_app.rightbutton": "fa fa-fighter-jet",
        "components_app.socialnetwork": "fa fa-gavel",
        "components_app.footerinfo": "fa fa-folder",
        "components_app.footerlinks": "fa fa-arrow-right",

        "main_app.homeabout": "nav-icon fa fa-window-maximize",
        "main_app.homeaboutqulayliklar": "fa fa-cog",
        "main_app.slider": "fa fa-history",
        "main_app.talimyonalishlari": "fa fa-wifi",
        "main_app.counter": "fa fa-toggle-on",
        "main_app.rahbariyat": "fa fa-thumbs-up",
        "main_app.video": "nav-icon fa fa-play-circle",
        "main_app.interaktivhizmatlar": "fa fa-th",
        "main_app.hamkorlar": "fa fa-list",
        "main_app.contactus": "fa fa-phone-alt",
        "main_app.contactuscard": "fa fa-phone-square-alt",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": "custom/custom.css",
    "custom_js": "custom/custom.js",
    # Whether to link font from fonts.googleapis.com (use custom_css to supply font otherwise)
    "use_google_fonts_cdn": True,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,

    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    # Add a language dropdown into the admin
    "language_chooser": False,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-info",
    "accent": "accent-teal",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": True,
    "sidebar_fixed": True,
    "sidebar": "sidebar-light-info",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "lux",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "actions_sticky_top": True
}