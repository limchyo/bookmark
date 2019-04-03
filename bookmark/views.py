from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Bookmark


# Create your views here.

# Bookmark 모델에 저장된 데이터를 모두 가져온다(목록 구현)
class BookmarkListView(ListView):
    model = Bookmark
    # 한 페이지에 출력되는 객체 수 설정
    paginate_by = 6

# Bookmark 모델에 데이터를 추가한다(추가 기능 구현)
class BookmarkCreateView(CreateView):
    model = Bookmark
    # 새로 추가될 데이터의 필드 설정
    fields = ['site_name', 'url']
    # success_url은 작성 후 이동할 페이지 설정
    # reverse_lazy는 제네릭뷰에서 사용하며, 생성시 list 이름의 url 패턴을 실행
    success_url = reverse_lazy('list')
    # 사용할 템플릿의 접미사 설정
    # _create 접미사가 있는 템플릿만 사용
    template_name_suffix = '_create'

# Bookmark 모델에 저장된 데이터의 상세페이지 구현
# 데이터를 그대로 출력하는 것이므로 별도의 가공 불필요
class BookmarkDetailView(DetailView):
    model = Bookmark

# 수정 기능 구현
class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

# 삭제 기능 구현
class BookmarkDeleteView(DeleteView):
    model = Bookmark
    # 삭제가 된 경우 메인페이지로 이동
    success_url = reverse_lazy('list')
