from django import forms
from django.utils.translation import \
    ugettext_lazy as _

from .models import Post


class PostAdminForm(forms.ModelForm):
    tags = forms.CharField(label=_('Tags'),
                           required=False,
                           widget=forms.TextInput())

    def __init__(self, *args, **kwargs):
        super(PostAdminForm, self).__init__(*args, **kwargs)
        if 'instance' in kwargs:
            self.fields['tags'].initial = ','.join(
                tag.name for tag in kwargs['instance'].tags.all())

    class Meta:
        model = Post
        fields = ['title',
                  'pub_date',
                  'content',
                  'tags',
                  'is_draft']
