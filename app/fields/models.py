from django.db import models


class Person(models.Model):
    SHIRT_SIZE = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField('이름', max_length=60)
    shirt_size = models.CharField(
        '셔츠 사이즈',
        max_length=1,
        choices=SHIRT_SIZE,
        help_text='S,M,L 중에 선택'
    )
    # 둘다 허용, 빈 값을 넣어도 이상없이 작동한다
    age = models.IntegerField('나이', blank=True, null=True)
    stars = models.IntegerField('좋아요', default=0)
    nickname = models.CharField(
        '닉네임',
        max_length=50,
        unique=True,
        blank=True,
        null=True,
    )
