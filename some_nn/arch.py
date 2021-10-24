import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy

X = numpy.random.uniform(-10, 10, 8 * 8 * 125).reshape(8, 8, -1)
print(X.shape)


# class CNN_first(nn.Module):
#     def __init__(self):
#         super(CNN_first, self).__init__()
#         self.conv1 = nn.Conv1d(in_channels=8, out_channels=8, kernel_size=8, stride=2)
#         self.maxPool = nn.MaxPool1d(kernel_size=4)
#         self.conv2 = nn.Conv1d(in_channels=8, out_channels=8, kernel_size=2, stride=2)
#
#     def forward(self, x):
#         x = self.conv1(x)
#         x = F.relu(x)
#         x = self.maxPool(x)
#         x = self.conv2(x)
#         x = self.maxPool(x)
#         x = F.relu(x)
#         output = F.log_softmax(x, dim=1)
#         return output


class CNN_second(nn.Module):
    def __init__(self):
        super(CNN_second, self).__init__()
        self.conv1 = nn.Conv1d(in_channels=8, out_channels=8, kernel_size=8, stride=2)
        self.conv2 = nn.Conv1d(in_channels=8, out_channels=8, kernel_size=2, stride=2)
        self.maxPool = nn.MaxPool1d(kernel_size=4)
        self.avgPool = nn.AvgPool1d(kernel_size=4)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.maxPool(x)
        x = self.conv2(x)
        x = self.avgPool(x)
        x = F.relu(x)
        output = F.log_softmax(x, dim=1)
        return output


model = CNN_second().double()
print(model(torch.tensor(X)).shape)
