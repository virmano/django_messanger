from django.db import models

# Create your models here.

class Comments(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    text = models.TextField()
    created_at = models.DateTimeField()
    has_reply = models.BooleanField(default=False)

    reply = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="replies"
    )


    def __str__(self):
        return f'{self.id}: {self.username}' if not self.reply else (f'{self.id}: {self.username} Reply to: '
                                                                         f'{self.reply.id}')
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"