import django_tables2 as tables
from .models import animal
from django_tables2.utils import Accessor as A
from .urls import *




class testTable(tables.Table):
    id = tables.Column(verbose_name='ID',linkify=True,visible=True)
    user_id = tables.Column(verbose_name='USER ID',visible=False)
    code = tables.Column(verbose_name='CODE',linkify=False)                     #column names must match model column names!!
    number = tables.Column(verbose_name='NUMBER',linkify=False)
    date = tables.Column(verbose_name='BIRTH DATE')
    gender = tables.Column(verbose_name='GENDER')
    image = tables.Column(verbose_name='IMAGE',visible=False)
    user = tables.Column(visible=False,verbose_name='USER EMAIL')
    
    

    class Meta:
        model = animal
        
        
  
     
    

