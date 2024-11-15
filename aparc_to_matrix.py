# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 14:40:24 2023

@author: sanga
"""

import os
#import re
import pandas as pd

# List of metrics
metrics_list = [
    'NumVert', 'SurfArea', 'GrayVol', 'ThickAvg', 'ThickStd',
    'MeanCurv', 'GausCurv', 'FoldInd', 'CurvInd'
]

# List of structure names
structure_names_list = [
    'bankssts', 'caudalanteriorcingulate', 'caudalmiddlefrontal', 'cuneus',
    'entorhinal', 'fusiform', 'inferiorparietal', 'inferiortemporal',
    'isthmuscingulate', 'lateraloccipital', 'lateralorbitofrontal', 'lingual',
    'medialorbitofrontal', 'middletemporal', 'parahippocampal', 'paracentral',
    'parsopercularis', 'parsorbitalis', 'parstriangularis', 'pericalcarine',
    'postcentral', 'posteriorcingulate', 'precentral', 'precuneus',
    'rostralanteriorcingulate', 'rostralmiddlefrontal', 'superiorfrontal',
    'superiorparietal', 'superiortemporal', 'supramarginal', 'frontalpole',
    'temporalpole', 'transversetemporal', 'insula'
]

#def extract_metrics(file_path):
file_path = 'C:\\Users\\sanga\\OneDrive\\Desktop\\Research\\Apostolova_Lab\\941_S_4420\\stats\\rh.aparc.stats'
def extract_metrics(file_path):
    
with open(file_path, 'r') as file:
    content = file.read()

metrics = {}
lines = content.strip().split('\n')
headers = None
structNames = []

for line in lines:
    if headers is None and line.startswith('# ColHeaders'):
        headers = line.split()[3:]
    elif headers is not None:
        structName = line.split()
        print(structName)
        #structNames.append(structName)
print(structName)
            
            structure_metrics = []
            for metric in headers:
                structure_metric = structName[0] + '_' + metric
                #structure_metrics.append(structure_metric)
                print(structure_metrics)
                if headers is not None:
                    metric_values = {header: value for header, value in zip(structure_metrics, structName[1:])}
                    metrics[structure_metric] = metric_values
                    #metrics.append(metric_values)
                    #print(metric_values)     
                
    return metrics


#def main(subject_folders):
# Create a dataframe with structure names and metrics

'''
for structure_name in structure_names_list:
    for metric in metrics_list:
        column_name = f"{structure_name}_{metric}"
        data.append({'Column': column_name, 'Value': None})
'''
data = []
df_structure_metrics = pd.DataFrame(data)

# Populate the dataframe with data values from rh.aparc.stats files
subject_folders = ['941_S_4420']
for subject_folder in subject_folders:
    stats_file = os.path.join(subject_folder, 'stats', 'rh.aparc.stats')

    if os.path.exists(stats_file):
        subject_name = os.path.basename(subject_folder)
        metrics = extract_metrics(stats_file)
        print(metrics)
        
        for structure_name in structure_names_list:
            for metric in metrics_list:
                column_name = f"{structure_name}_{metric}"
                data_value = metrics.get(structure_name, {}).get(metric, None)
                df_structure_metrics.loc[
                    df_structure_metrics['Column'] == column_name, 'Value'
                ] = data_value
    else:
        print(f"Stats file not found for subject {subject_folder}")

# Reshape the dataframe to have structure_metric columns as rows
df_structure_metrics = df_structure_metrics.pivot(index=None, columns='Column', values='Value')

# Save the dataframe to an Excel file
df_structure_metrics.to_excel('rh.aparc.stats.xlsx', index=False)

if __name__ == '__main__':
    subject_folders = [
        '/path/to/subject1',
        '/path/to/subject2',
        # Add more subject folders as needed
    ]
    
    main(subject_folders)
