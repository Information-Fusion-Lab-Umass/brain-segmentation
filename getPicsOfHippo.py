import os
import pandas as pd
from datetime import datetime

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
FSL_DIR = os.path.join(SCRIPT_DIR, 'fsl')
RFA = os.path.join(FSL_DIR, 'bin', 'run_first_all')
OUTPUT_DIR = os.path.join(SCRIPT_DIR, 'output')

paths = pd.read_csv(os.path.join(SCRIPT_DIR, 'mriimg_meta_v5.csv'))['caps_path']

limit = int(os.environ['BS_LIMIT'])
if limit is not None:
    paths = paths[:limit]

for path in paths:
	parts = os.path.basename(path).replace('.nii.gz', '').split('_')
	patient_id = parts[0].replace('sub-ADNI', '')
	viscode = parts[1].replace('ses-', '').lower()
	output_dir = os.path.join(OUTPUT_DIR, patient_id, viscode)

	os.makedirs(output_dir, exist_ok=True)
	os.chdir(output_dir)
	os.system(f'{RFA} -i {path} -s L_Hipp,R_Hipp')

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(f"We did it!\nFinished at: {current_time}")
