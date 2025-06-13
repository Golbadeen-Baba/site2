from django.db import models

class ModelApplicant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    instagram_handle = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.instagram_handle}"


class ModelQuestionnaire(models.Model):
    q1 = models.CharField(max_length=255, verbose_name="Modeling niche")
    q2 = models.TextField(verbose_name="Photoshoot preparation")
    q3 = models.TextField(verbose_name="Comfort with traditional attire")
    q4 = models.TextField(blank=True, verbose_name="Creative concepts/themes")
    q5 = models.TextField(blank=True, verbose_name="Preferred timeframe")
    q6 = models.TextField(blank=True, verbose_name="Openness to diverse locations")
    q7 = models.TextField(blank=True, verbose_name="Usual shoot rates")

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Questionnaire - {self.id}"
