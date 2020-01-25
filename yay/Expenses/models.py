from django.db import models

# Create your models here.

class Device(models.Model):

    Title = models.CharField(max_length=255, blank=False, default='')
    Value = models.CharField(max_length=255, default='')
    Image = models.FileField(blank=True)

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

class Desktops(Device):
    pass

class Laptops(Device):
    pass

class Mobiles(Device):
    pass