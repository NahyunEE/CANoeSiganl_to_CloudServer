from django.db import models

# Create your models here.
class Module(models.Model):
 
    #max_digit =허용자릿수
    #decimal_palce = 소수점 아래값
       
  
     # Cell 0 attributes
    cell0_soc = models.DecimalField(max_digits=5, decimal_places=2, help_text="State of Charge for Cell 0")
    cell0_voltage = models.DecimalField(max_digits=5, decimal_places=2, help_text="Voltage for Cell 0")
    # Cell 1 attributes
    cell1_soc = models.DecimalField(max_digits=5, decimal_places=2, help_text="State of Charge for Cell 1")
    cell1_voltage = models.DecimalField(max_digits=5, decimal_places=2, help_text="Voltage for Cell 1")
     # Cell 2 attributes
    cell2_soc = models.DecimalField(max_digits=5, decimal_places=2, help_text="State of Charge for Cell 2")
    cell2_voltage = models.DecimalField(max_digits=5, decimal_places=2, help_text="Voltage for Cell 2")
    # Cell 3 attributes
    cell3_soc = models.DecimalField(max_digits=5, decimal_places=2, help_text="State of Charge for Cell 3")
    cell3_voltage = models.DecimalField(max_digits=5, decimal_places=2, help_text="Voltage for Cell 3")
    
    #Charging Flag
    charge_flag = models.DecimalField(max_digits=5, decimal_places=2, help_text="Charge Flag")
    
    #temperature 
    temperature = models.DecimalField(max_digits=5, decimal_places=2, help_text="Charge Flag")
    
    def __str__(self):
        return f"Module ID: {self.moduleId}"