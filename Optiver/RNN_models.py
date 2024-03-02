from torch import nn

class GRUNet(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, n_layers, drop_prob=0.2):
        super(GRUNet, self).__init__()
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        self.n_layers = n_layers
        self.drop_rate = drop_prob

        self.gru = nn.GRU(self.input_dim,self.hidden_dim,self.n_layers,
                          batch_first = True, dropout=self.drop_rate)
        
        self.fc = nn.Linear(hidden_dim, output_dim)
        self.act = nn.ReLU()
    
    def forward(self, x, h):
        out,h = self.gru(x,h)
        out = self.fc(self.act(out))
        return out, h
    
    def init_hidden(self, batch_size):
        weight = next(self.parameters()).data
        hidden = weight.new(self.n_layers, batch_size, self.hidden_dim).zero_().to('cuda')
        return hidden
    
class LSTMNet(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, n_layers, drop_prob=0.2):
        super(LSTMNet, self).__init__()
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        self.n_layers = n_layers
        self.drop_rate = drop_prob

        self.lstm = nn.LSTM(self.input_dim,self.hidden_dim,self.n_layers,
                            batch_first=True,dropout=self.drop_rate)
        self.fc = nn.Linear(hidden_dim,output_dim)
        self.act = nn.ReLU()

    def forward(self,x,h):
        out,h = self.lstm(x,h)
        out = self.fc(self.act(out))
        return out, h
    
    def init_hidden(self, batch_size):
        weight = next(self.parameters()).data
        hidden = (weight.new(self.n_layers, batch_size, self.hidden_dim).zero_().to('cuda'),
                  weight.new(self.n_layers, batch_size, self.hidden_dim).zero_().to('cuda'))
        return hidden


        
