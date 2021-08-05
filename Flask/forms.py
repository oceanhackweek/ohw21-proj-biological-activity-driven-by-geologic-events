from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms import SelectField
from wtforms.validators import DataRequired

class QueryInputForm(FlaskForm):
    start_date = DateField('Start Date', id = 'start_date', validators = [DataRequired()], format = '%Y-%m-%d')
    end_date = DateField('End Date', id = 'end_date', validators = [DataRequired()], format = '%Y-%m-%d')
    select_var = SelectField('Select a Feature', id = 'select_var', validators = [DataRequired()], 
                            choices = [('iespres', 'Seafloor Pressure'), 
                                        ('sea_water_ph_reported_on_total_scale', 'pH'), 
                                        ('sea_water_temperature', 'Temperature'),
                                        ('sea_water_practical_salinity', 'Salinity'),
                                        ('mole_concentration_of_dissolved_molecular_oxygen_in_sea_water', 'Dissolved Oxygen'),
                                        ('mass_concentration_of_chlorophyll_a_in_sea_water', 'Chlorophyll a'),
                                        ('sea_water_density', 'Density'),
                                        ('sea_water_pressure', 'Water Pressure')])