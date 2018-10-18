from django.db import models

__all__ = (
    'RelatedUser',
    'PostBase',
    'PhotoPost',
    'TextPost',
)


class RelatedUser(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PostBase(models.Model):
    author = models.ForeignKey(
        RelatedUser,
        on_delete=models.CASCADE,
        # 유저(Person) 입장에서
        # 자신이 특정 Post의 'author'인 경우에 해당하는 모든 PostBase 객체를 참조하는 역방향 매니저 이름
        # %(class)s     : 상속받은 클래스명의 소문자화
        # %(app_label)s : 상속받은 클래스가 속한 애플리케이션명의 소문자화
        related_name='%(app_label)s_%(class)s_set',
        related_query_name='%(app_label)s_%(class)s',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class PhotoPost(PostBase):
    # author의 related_name
    #   abstract_base_classes_photopost_set
    photo_url = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'Post (author: {self.author.name})'


class TextPost(PostBase):
    # author의 related_name
    #  textpost_set
    text = models.TextField(blank=True)

    def __str__(self):
        return f'Post (author: {self.author.name})'
