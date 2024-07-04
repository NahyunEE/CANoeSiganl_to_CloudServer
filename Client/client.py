import requests 
import time
import random

# Import CANoe module
from py_canoe import CANoe
server_url = "http://52.78.227.179:8000/update/"
#server_url = "http://127.0.0.1:8000/update/"
moduleid = 1

num=0
# create CANoe object
canoe_inst = CANoe()

# open CANoe configuration. Replace canoe_cfg with yours.
canoe_inst.open(canoe_cfg=r'C:\workspace\Cannoe\bms\bms.cfg')

# print installed CANoe application version
canoe_inst.get_canoe_version_info()

# Start CANoe measurement
canoe_inst.start_measurement()




while True:
   
   
    cell0_voltage = canoe_inst.get_signal_value('CAN', 1, 'msg_cell0_data', 'sig_mon_cell0_voltage')
    
    cell1_voltage = canoe_inst.get_signal_value('CAN', 1, 'msg_cell1_data', 'sig_mon_cell1_voltage')
   
    cell2_voltage = canoe_inst.get_signal_value('CAN', 1, 'msg_cell2_data', 'sig_mon_cell2_voltage')
   
    cell3_voltage = canoe_inst.get_signal_value('CAN', 1, 'msg_cell3_data', 'sig_mon_cell3_voltage')
   
    temperature = canoe_inst.get_signal_value('CAN', 1, 'msg_temperature', 'sig_temperature')
   # temperature = random.uniform(0, 100)
    
    chargeFlag = canoe_inst.get_signal_value('CAN', 1, 'msg_chargingFlag', 'sig_chargingFlag')
    
    
    
    sensor_data = {
      
        'cell0_voltage':cell0_voltage,
        'cell1_voltage': cell1_voltage,
        'cell2_voltage':cell2_voltage,
        'cell3_voltage': cell3_voltage,
        'temperature': temperature,
        'chargeFlag':chargeFlag,      
    }
    response = requests.post(server_url, data=sensor_data)
    
    time.sleep(2)
    
    if response.status_code == 200:
        print("Data sent successfully")
    else:
        print("Failed to send data")














