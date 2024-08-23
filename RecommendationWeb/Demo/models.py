from django.db import models

class FieldOfStudy(models.Model):
    ID = models.CharField(max_length=3, primary_key=True)
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

class University(models.Model):
    ID = models.CharField(max_length=3, primary_key=True)
    Name = models.CharField(max_length=200)
    Type = models.CharField(max_length=100)
    Description = models.TextField(null=True, blank=True)
    Logo = models.ImageField(upload_to='logos/')
    Min_Score = models.DecimalField(max_digits=4, decimal_places=2)
    Max_Score = models.DecimalField(max_digits=4, decimal_places=2)
    Website = models.URLField() 
    Facebook = models.URLField()
    Fields = models.ManyToManyField(FieldOfStudy ,related_name='universities')

    def __str__(self):
        return self.Name
    
class Major(models.Model):
    ID = models.CharField(max_length=7, primary_key=True)
    FieldID= models.ForeignKey(FieldOfStudy, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)

    def __str__(self):
        return self.Name

class UniMajor(models.Model):
    UniID = models.ForeignKey(University, on_delete=models.CASCADE)
    MajorID = models.ForeignKey(Major, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)
    Score = models.DecimalField(max_digits=4, decimal_places=2)
    Tuition_Fee = models.DecimalField(max_digits=12, decimal_places=0)
    Subject_combination = models.CharField(max_length=3)

    def formatted_tuition_fee(self):
        return "{:,.0f}".format(self.Tuition_Fee)
    
    def __str__(self):
        return str(self.Score)