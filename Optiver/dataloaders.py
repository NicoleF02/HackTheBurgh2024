from torch.utils.data import Dataset
import torch
import pandas as pd
import numpy as np

class Trading_History_Dataset(Dataset):
    def __init__(self,filename,indices=None,window_size=50):
        super(Trading_History_Dataset,self).__init__()
        trade_history = pd.read_csv(filename).iloc[:,0:-1].apply(lambda x: (x-x.mean())/ x.std(), axis=0)

        columns = trade_history.columns
        label_columns = [name for name in columns if 'best' in name]
        data_columns = [name for name in columns if 'last' in name]

        window_size = window_size
        data_windows = []
        label_windows = []
        for base in range(0,len(trade_history)-window_size):
            data_sliding_window = trade_history[data_columns][base:base+window_size]
            data_windows.append(data_sliding_window.values)
            label_sliding_window = trade_history[label_columns][base:base+window_size]
            label_windows.append(label_sliding_window.values)

        if indices is not None:
            self.data_windows = torch.Tensor(np.stack(data_windows))[indices]
            self.label_windows = torch.Tensor(np.stack(label_windows))[indices]
        else:
            self.data_windows = torch.Tensor(np.stack(data_windows))
            self.label_windows = torch.Tensor(np.stack(label_windows))

    def __getitem__(self, index):
        return self.data_windows[index], self.label_windows[index]
    
    def __len__(self):
        return len(self.data_windows)
