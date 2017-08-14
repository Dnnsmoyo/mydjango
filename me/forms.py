from django.forms import ModelForm
from  me.models import Post

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['author','title','content','date_published']
        order_by = 'date_published'