#import ast; ast.parse(open('app.py').read()); print('app.py syntax OK')


#to check tabular input dimension expected by the model checkpoint
#import torch
#from pathlib import Path

## Load model checkpoint
#model_path = Path("models/federated_best_fedavg.pth")
#checkpoint = torch.load(model_path, map_location='cpu')

## Find tabular branch first layer
#for key in checkpoint['model_state_dict'].keys():
    #if 'tabular_branch' in key and 'weight' in key:
        #weight_shape = checkpoint['model_state_dict'][key].shape
        #print(f"{key}: {weight_shape}")
        #if 'tabular_branch.0.weight' in key or 'tabular_branch.1.weight' in key:
            #print(f"\n⚠️ MODEL EXPECTS {weight_shape[1]} TABULAR FEATURES")
            #break


import torch

print(torch.device("cuda" if torch.cuda.is_available() else "cpu"))