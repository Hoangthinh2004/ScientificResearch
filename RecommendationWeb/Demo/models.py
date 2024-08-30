from django.db import models

class FieldOfStudy(models.Model):
    ID = models.CharField(max_length=3, primary_key=True)
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.ID

class University(models.Model):
    ID = models.CharField(max_length=3, primary_key=True)
    Name = models.CharField(max_length=200)
    Type = models.CharField(max_length=100)
    Description = models.TextField(max_length=5000, null=True, blank=True)
    Logo = models.ImageField(upload_to='logos/')
    Min_Score = models.DecimalField(max_digits=4, decimal_places=2)
    Max_Score = models.DecimalField(max_digits=4, decimal_places=2)
    Min_Tuition_Fee = models.DecimalField(max_digits=6, decimal_places=0, null=True, blank=True)
    Max_Tuition_Fee = models.DecimalField(max_digits=9, decimal_places=0, null=True, blank=True)
    Website = models.URLField() 
    Facebook = models.URLField()
    Score_Link = models.URLField(null=True, blank=True)

    def formatted_tuition_fee(self):
        return f"{self.Min_Tuition_Fee:,.0f} - {self.Max_Tuition_Fee:,.0f}"

    def __str__(self):
        return self.Name
    
class UniField(models.Model):
    Uni = models.ForeignKey(University, on_delete=models.CASCADE)
    Field = models.ForeignKey(FieldOfStudy, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Uni.Name} - {self.Field.Name}"
    
class Major(models.Model):
    ID = models.CharField(max_length=7, primary_key=True)
    FieldID= models.ForeignKey(FieldOfStudy, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)

    def __str__(self):
        return self.ID

class UniMajor(models.Model):
    UniID = models.ForeignKey(University, on_delete=models.CASCADE)
    MajorID = models.ForeignKey(Major, on_delete=models.CASCADE)
    U_Name = models.CharField(max_length=100, null=True, blank=True)
    M_Name = models.CharField(max_length=200)
    Tuition_Fee = models.DecimalField(max_digits=12, decimal_places=0, null=True, blank=True)

    def formatted_tuition_fee(self):
        return "{:,.0f}".format(self.Tuition_Fee)
    
    def __str__(self):
        return str(self.Score)
    
class Combination(models.Model):
    ID = models.CharField(max_length=3, primary_key=True)
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.ID
    
class CombMajor(models.Model):
    Uni = models.ForeignKey(University, on_delete=models.CASCADE)
    Major = models.ForeignKey(Major, on_delete=models.CASCADE)
    Comb = models.ForeignKey(Combination, on_delete=models.CASCADE)
    Score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.Uni.ID} - {self.Major.ID} - {self.Comb.ID} - {self.Score}"

    
class Region(models.Model):
    ID = models.CharField(max_length=3, primary_key=True)
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name
    
class Campus(models.Model):
    Uni = models.ForeignKey(University, on_delete=models.CASCADE)
    Region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Un.Name} - {self.Region.Name}"