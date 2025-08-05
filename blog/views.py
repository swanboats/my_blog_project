from django.shortcuts import render, get_object_or_404
from .models import Post

# 記事一覧表示ビュー
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # 新しい順に取得
    return render(request, 'blog/post_list.html', {'posts': posts})

# 記事詳細表示ビュー
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  # 存在しない記事なら404エラー
    return render(request, 'blog/post_detail.html', {'post': post})
