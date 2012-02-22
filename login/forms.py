from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


class AuthenticationForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {'placeholder': _('Username ...')}
        self.fields['password'].widget.attrs = {'placeholder': _('Password ...')}
