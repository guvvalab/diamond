from django.db import models
# Create your models here.
class JuiceMenu(models.Model):
	s_no = models.AutoField(primary_key=True)
	item_name = models.CharField(max_length= 50)
	item_price = models.FloatField()

	def __str__(self):
		return self.item_name + ' - '+ str(self.item_price)	