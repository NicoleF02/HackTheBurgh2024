import pandas as pd
import numpy as np
from RNN_models import *
from dataloaders import Trading_History_Dataset
from torch.utils.data import DataLoader
import torch

if __name__ == "__main__":
    full_dataset = Trading_History_Dataset('trade_history_data.csv',window_size=10)
    length = len(full_dataset.data_windows)
    indices = np.random.permutation(range(length))
    batch_size = 64

    train_idxs = indices[:int(length*0.6)]
    valid_idxs = indices[int(length*0.6):int(length*0.8)]
    test_idxs = indices[int(length*0.8):]

    train_dataset = Trading_History_Dataset('trade_history_data.csv',train_idxs,window_size=10)
    valid_dataset = Trading_History_Dataset('trade_history_data.csv',valid_idxs,window_size=10)
    test_dataset = Trading_History_Dataset('trade_history_data.csv',test_idxs,window_size=10)

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True,drop_last=True)
    valid_loader = DataLoader(valid_dataset, batch_size=batch_size, shuffle=True,drop_last=True)
    test_dataset = DataLoader(test_dataset, batch_size=batch_size, shuffle=True,drop_last=True)

    epochs = 100
    hidden_dim = 128
    n_layers = 2

    input_dim = next(iter(train_loader))[0].shape[2]
    output_dim = next(iter(train_loader))[1].shape[2]

    model = GRUNet(input_dim,hidden_dim,output_dim,n_layers,0.3).to('cuda')

    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    
    for epoch in range(0, epochs):
        model.train()
        avg_loss = 0
        batches = 0
        h = model.init_hidden(batch_size)
        
        for datas,labels in train_loader:
            batches += 1
            model.zero_grad()
            out,hiddens = model(datas.to('cuda').float(),h)
            loss = criterion(out, labels.to('cuda').float())
            
            loss.mean().backward()
            optimizer.step()

            avg_loss += loss.mean().item()
        print(f"Epoch:{epoch} | Train MSE Loss: {avg_loss/batches}")

        model.eval()
        batches = 0
        avg_loss = 0
        h = model.init_hidden(batch_size)
        for datas, labels in valid_loader:
            batches += 1
            model.zero_grad()
            out,hiddens = model(datas.to('cuda').float(),h)
            loss = criterion(out, labels.to('cuda').float())

            avg_loss += loss.mean().item()
        print(f"Epoch:{epoch} | Valid MSE Loss: {avg_loss/batches}")
