from django.forms import ModelForm

from instagram.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        # fiields = "__all___"
        fields = ['message', 'is_public']

# """form ㅂㅏㅇ식"""
# form = PostForm(request.POST)
# if form.is_valid():
#     post = form.save(commit=False)
#     post.author = request.user
#     post.ip = request.META['REMOTE_ADDR']
#     post.save()

# """"seriallizer 방식"""
# serializer.is_valid(...)
# serializer.save(author=request.user, ip=request.META['REMOTE_ADDR'])
