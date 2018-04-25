from django.conf import settings
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

class Lawyer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=30, help_text='한글성명을 입력해주세요.', verbose_name='성명(한글)')
    name_en = models.CharField(max_length=30, help_text='영문성명을 입력해주세요.', verbose_name='성명(영문)')
    email_address = models.EmailField(help_text='이메일주소를 입력해주세요.')
    address = models.CharField(max_length=100, help_text='사무실 주소를 입력해주세요.', blank=True)
    phone = models.CharField(blank=True, max_length=20, help_text='전화번호를 입력해주세요.')
    fax = models.CharField(max_length=50, blank=True, help_text='팩스번호를 입력해주세요.')
    unique_url = models.CharField(max_length=50, unique=True, help_text='주소에 사용될 영문자(대소문자구분)를 작성해주세요 (ex)영문성함, 사무소이름 등')
    profile_image = ProcessedImageField(blank=True, upload_to='lawyer/%Y/%m/%d',
                                processors=[Thumbnail(300,400)], 
                                format='JPEG', options={'quality':70})
    fields = models.CharField(blank=True, max_length=50, help_text='관련업무분야를 선택해주세요.')
    intro = models.TextField(blank=True, help_text='"000변호사의 주된 업무분야는 xx,xx,xx 입니다. 0변호사는 ~한 활동을 하고 있고 ---."와 같은 형식으로 입력해주세요.', verbose_name='소개')
    p_certificate = models.CharField(max_length=50, help_text='년도/자격을 작성해주세요. 예시)2004/변호사(대한민국)', verbose_name='자격취득')
    p_edu = models.TextField(blank=True, help_text='학력사항을 작성해주세요.', verbose_name='학력')
    p_story = models.TextField(blank=True, help_text='경력 사항을 작성해주세요.', verbose_name='경력')
    p_activity = models.TextField(blank=True, help_text='저서/활동을 작성해주세요.', verbose_name='저서/활동')
    p_prize = models.TextField(blank=True, help_text='수상내역을 작성해주세요.', verbose_name='수상')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('lawyer:lawyer_detail', args=[self.unique_url])