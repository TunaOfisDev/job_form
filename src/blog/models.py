from accounts.models import CustomUser
from django.db import models

STATUS = (
    (0, "Taslak"),
    (1, "Yayınla"),
    (2, "Arşiv"),
)


class Post(models.Model):
    task_title       = models.CharField(max_length=255, verbose_name="Görev Başlık")
    project_name     = models.CharField(max_length=255, blank=True, verbose_name="Proje Adı")
    deadline         = models.DateTimeField(auto_now=False ,verbose_name="Tarih")
    task_description = models.TextField(verbose_name="Görev Açıklamaları")
    status           = models.IntegerField(choices=STATUS, default=1)

    author = models.ForeignKey(
        CustomUser,
        related_name="blog_posts",
        on_delete=models.CASCADE,
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_title





