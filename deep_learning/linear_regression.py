import numpy as np
import torch
import torch.nn as nn

# Input (temp, rainfall, humidity)
inputs = np.array([[73, 67, 43], [91, 88, 64], [87, 134, 58], [102, 43, 37], [69, 96, 70], [73, 67, 43], [91, 88, 64], [87, 134, 58], [102, 43, 37], [69, 96, 70], [73, 67, 43], [91, 88, 64], [87, 134, 58], [102, 43, 37], [69, 96, 70]], dtype='float32')
# Targets (apples, oranges)
targets = np.array([[56, 70], [81, 101], [119, 133], [22, 37], [103, 119], 
                    [56, 70], [81, 101], [119, 133], [22, 37], [103, 119], 
                    [56, 70], [81, 101], [119, 133], [22, 37], [103, 119]], dtype='float32')

inputs = torch.from_numpy(inputs)
targets = torch.from_numpy(targets)

# Import tensor dataset & data loader
from torch.utils.data import TensorDataset, DataLoader

# Define dataset
train_ds = TensorDataset(inputs, targets) # 1000
print(train_ds[:])

def collate_fn(data):
    data += 5
    return data
# Define data loader
batch_size = 5
train_dl = DataLoader(train_ds, batch_size, collate_fn=collate_fn, shuffle=True)
next(iter(train_dl))

# Define model
model = nn.Linear(3, 2)
print(model.weight)
print(model.bias)

# hyper parameter: so layer, learning rate, hidden size 
class Multilayer(nn.Module):
    def __init__(self, in_dim=3, out_dim=2, hidden_size = 10) -> None:
        super().__init__()
        self.layer1 = nn.Linear(3, hidden_size)
        self.layer2 = nn.Linear(hidden_size, 2)
    def forward(self, x):
        z = self.layer1(x)
        y = self.layer2(z)
        return y, z
model = Multilayer(in_dim=3, out_dim=2, hidden_size=10)

# Define optimizer
opt = torch.optim.AdamW(model.parameters(), lr=1e-5)

# Import nn.functional
import torch.nn.functional as F

# Define loss function
loss_fn = F.mse_loss
# loss_fn2 = F.mse_loss
# # loss_fn = nn.MSELoss()
# loss1 = loss_fn(model(inputs)[0], targets)
# loss2 = loss_fn2(model(inputs)[1], target_z)
# loss = loss1 + loss2
# print(loss)

# Define a utility function to train the model
def fit(num_epochs, model, loss_fn, opt):
    for epoch in range(num_epochs):
        for xb,yb in train_dl:
            # Generate predictions
            pred = model(xb)
            loss = loss_fn(pred, yb)
            # Perform gradient descent
            loss.backward()
            opt.step()
            opt.zero_grad()
    print('Training loss: ', loss_fn(model(inputs), targets))
    
# Train the model for 100 epochs
fit(100, model, loss_fn, opt)

# Generate predictions
preds = model(inputs)
