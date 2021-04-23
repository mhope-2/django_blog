from django import forms
from blog.models import Post

class CreateBlogForm(forms.ModelForm):
    title = forms.CharField(max_length=255)
    body = forms.CharField(widget=forms.Textarea)
    # url = forms.URLField(widget=forms.TextInput(attrs={'placeholder': 'Enter URL', 'size':'12', 'class': "form-control"}),label='URL')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['body'].required = True
        
    class Meta:
        verbose_name = 'blog'
        model = Post
        fields = ('author','title', 'body')





