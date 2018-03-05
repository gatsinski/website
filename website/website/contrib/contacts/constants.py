from django.utils.translation import ugettext_lazy as _


FACEBOOK = 'facebook'
TWITTER = 'twitter'
GOOGLE_PLUS = 'google-plus'
LINKEDIN = 'linkedin'
GITHUB = 'github'
SKYPE = 'skype'
EMAIL = 'email'
PHONE = 'phone'

CONTACT_ICON_CHOICES = (
    (FACEBOOK, _('Facebook')),
    (TWITTER, _('Twitter')),
    (GOOGLE_PLUS, _('Google Plus')),
    (LINKEDIN, _('LinkedIn')),
    (SKYPE, _('Skype')),
    (EMAIL, _('Email')),
    (GITHUB, _('Github')),
    (PHONE, _('Phone'))
)

ICON_MAP = {
    FACEBOOK: 'facebook',
    TWITTER: 'twitter',
    GOOGLE_PLUS: 'google-plus',
    LINKEDIN: 'linkedin',
    SKYPE: 'skype',
    EMAIL: 'envelope',
    GITHUB: 'github',
    PHONE: 'phone'
}
