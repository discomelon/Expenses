from django.db import models
from datetime import date
# Create your models here.

class Entity(models.Model):

    Title = models.CharField(max_length=255, blank=False, default='')
    Value = models.CharField(max_length=255, default='')
    Image = models.FileField(blank=True)
    Date = models.DateField(auto_now_add=False, auto_now=False, blank = True)
    Time = models.DateField(auto_now_add=True, auto_now=False, blank = True)

    EXCEL_CHOICES = ( 
     ('Work', 'Work'),
     ('Charity', 'Charity'),
     ('Tax', 'Tax'),
     ('Water', 'Water'),
     ('Council', 'Council'),
     ('Insurance', 'Insurance'),
     ('Land Tax', 'Land Tax'),
     ('Repairs', 'Repairs'),
     ('Sundry', 'Sundry'),
     ('Interest', 'Interest'),
     ('Garden', 'Garden'),
     ('Property Agent', 'Property Agent'),
     ('Borrowing', ' Borrowing'),
     ('Depreciation', 'Depreciation'),
     ('Pest', 'Pest'),
     ('Advertising', 'Advertising'),
     (' Stationary', 'Stationary'),
     ('Telephone', 'Telephone'),
     ('Postage', 'Postage'),
     (' Electicity', 'Electicity'),
     ('Gas', 'Gas'),
     ('Conveyancing', 'Conveyancing'),
     )


    Category = models.CharField(max_length=255, choices=EXCEL_CHOICES, default='None')
    Description = models.CharField(max_length=255, default="No Issues")


    class Meta:
        abstract = True

    def __str__(self):
        return 'Title: {0} Value: {1}'.format(self.Title, self.Value)

class Farhan(Entity):
    pass

class Nadia(Entity):
    pass

class FarhanFamilySuperFund(Entity):
    pass

class Ongie(Entity):
    pass

class OrangeTrust(Entity):
    pass

