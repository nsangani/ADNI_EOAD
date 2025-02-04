# -*- coding: utf-8 -*-

import os
cwd = os.chdir('path_to_dir\\MRI_QC_scripts')

filename = [
    'E001_V1_2008-10-02_denoised.nii',
    'E001_V2_2009-10-16_denoised.nii',
    'E057_V5_2013-06-03_denoised.nii',
    'E058_V1_2009-04-23_denoised.nii',
    ]

for i in filename:
    file_name = i[:7]
    
    with open(file_name + '.sh', 'w') as script_file:
    
        script_file.write('#!/bin/sh\n')
        script_file.write(f'#SBATCH -J {file_name}\n')
        script_file.write('#SBATCH -p general\n')
        script_file.write('#SBATCH -o %j.txt\n')
        script_file.write('#SBATCH -e %j.err\n')
        script_file.write('#SBATCH --mail-type=END,FAIL\n')
        script_file.write('#SBATCH --mail-user=nsangani@iu.edu\n')
        script_file.write('#SBATCH --nodes=1\n')
        script_file.write('#SBATCH --ntasks-per-node=16\n')
        script_file.write('#SBATCH --time=24:00:00\n')
        script_file.write('#SBATCH --mem=15gb\n')
        script_file.write('#SBATCH -A general\n\n')
        
        script_file.write('module load freesurfer/7.4.1\n')
        
        script_file.write('recon-all ' + i)

    
# Open the 'superscript.txt' file in append mode
with open('superscript.sh', 'a') as script_file:
    # Loop through each filename in the list
    for i in filename:
        # Extract the first 7 characters and add '.txt'
        file_name = i[:7] + '.txt'
        
        # Write the filename to the file, preceded by 'sbatch ' and followed by a newline
        script_file.write('sbatch ' + file_name + '\n')
        

PET_subject = [
    'E001'
    'E004'
    'E005'
    'E006'
    ]
        
# Open the dcm2nii file in append mode
with open('dcm2nii_pet_IMAGENE.sh', 'a') as script_file:
    # Loop through each filename in the list
    for i in PET_subject:
        
        # Write the dcm2niix to filename
        script_file.write('dcm2niix ' + i + '\n')
            
        
