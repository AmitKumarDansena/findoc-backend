from django.db import models

class PageLinks(models.Model):
    ipo_url = models.URLField("IPO Page URL")
    rne_url = models.URLField("Refer & Earn Page URL")

    def __str__(self):
        return "Findoc Page Links"
