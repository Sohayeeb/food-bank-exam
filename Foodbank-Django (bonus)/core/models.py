from django.db import models

class Family(models.Model):
    family_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    members = models.PositiveIntegerField()
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.family_id

class FoodStock(models.Model):
    packs = models.IntegerField(default=0)

    def __str__(self):
        return f"Stock: {self.packs}"

class Distribution(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    packs = models.IntegerField()
    distributed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.family.family_id} - {self.packs}"
