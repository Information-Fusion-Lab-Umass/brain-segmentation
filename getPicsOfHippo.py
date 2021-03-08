import os
import pandas as pd
from datetime import datetime

SCRIPT_DIR = os.path.dirname(__file__)

df = pd.read_csv('mriimg_meta_v5.csv')['caps_path']

for path in paths:
	parts = os.path.basename(path).replace('.nii.gz', '').split('_')
	patient_id = parts[0].replace('sub-ADNI', '')
	visitCode = parts[1].replace('ses-', '').lower()
	outputPath = os.path.join('./', patient_id, viscode))
	os.makedirs(outputPath, exit_ok=True)
	os.chrpath(outputPath)
	os.system(f'run_first_all -i {path} -s L_Hipp,R_Hipp')
	os.chrpath('./../../')

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(f"We did it!\nFinished at: {current_time}")