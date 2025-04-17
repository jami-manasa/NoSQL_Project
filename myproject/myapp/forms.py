from django import forms
from .models import MentorshipPost

class MentorshipPostForm(forms.ModelForm):
    class Meta:
        model = MentorshipPost
        fields = ['username', 'title', 'description', 'mentorship_type', 'expertise_area']
        widgets = {
            'mentorship_type': forms.Select(choices=MentorshipPost.MENTORSHIP_TYPE_CHOICES),
            'description': forms.Textarea(attrs={'rows': 4}),
        }
