from django.views import generic
from blog.models import Post

class PostView(generic.ListView): 

    # pega os posts publicados com status de 'publish' e ordena eles de acordo com a data de criacao, armazena eles na variavel queryset
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'