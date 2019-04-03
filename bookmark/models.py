from django.db import models
from django.urls import reverse

# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        return "이름 : {}, 주소 : {}".format(self.site_name, self.url)

    # 객체의 상세페이지 주소를 반환하는 메서드이다
    def get_absolute_url(self):
        # detail 이름의 url 패턴에서 id 값에 해당하는 url 출력
        return reverse('detail', args=[str(self.id)])
