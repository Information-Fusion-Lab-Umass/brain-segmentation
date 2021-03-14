import os
import pandas as pd
from datetime import datetime

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
RFA = os.path.expanduser(os.path.join('~', 'Downloads', 'fsl', 'bin', 'run_first_all'))

paths = pd.read_csv(os.path.join(SCRIPT_DIR, 'mriimg_meta_v5.csv'))['caps_path']

limit = int(os.environ['BS_LIMIT'])
if limit is not None:
    paths = paths[:limit]

for path in paths:
	parts = os.path.basename(path).replace('.nii.gz', '').split('_')
	patient_id = parts[0].replace('sub-ADNI', '')
	viscode = parts[1].replace('ses-', '').lower()
	outputPath = os.path.join(SCRIPT_DIR, 'output', patient_id, viscode)

	os.makedirs(outputPath, exist_ok=True)
	os.chdir(outputPath)
	os.system(f'{RFA} -i {path} -s L_Hipp,R_Hipp')

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(f"We did it!\nFinished at: {current_time}")
