import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.utils.data as torch_data


class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv1d(in_channels=8, out_channels=20, kernel_size=4)
        self.conv2 = nn.Conv1d(in_channels=20, out_channels=50, kernel_size=2)
        self.conv3 = nn.Conv1d(in_channels=50, out_channels=122, kernel_size=1)
        self.conv4 = nn.Conv1d(in_channels=122, out_channels=8, kernel_size=1)
        self.maxPool = nn.MaxPool1d(1)
        self.avgPool = nn.AvgPool1d(1)
        self.drop = nn.Dropout(0.25)
        self.fc1 = nn.Linear(9216, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = self.maxPool(x)
        x = self.conv3(x)
        x = F.relu(x)
        x = self.conv4(x)
        x = F.relu(x)
        x = self.avgPool(x)
        x = self.drop(x)
        output = F.log_softmax(x, dim=1)
        return output


def train(model, device, train_loader, optimizer, epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = F.nll_loss(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % 10 == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                       100. * batch_idx / len(train_loader), loss.item()))


def test(model, device, test_loader):
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            test_loss += F.nll_loss(output, target, reduction='sum').item()
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(target.view_as(pred)).sum().item()

    test_loss /= len(test_loader.dataset)

    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))


def main():
    epochs = 14
    torch.manual_seed(1)

    use_cuda = torch.cuda.is_available()
    device = torch.device("cuda" if use_cuda else "cpu")

    kwargs = {'num_workers': 1, 'pin_memory': True} if use_cuda else {}

    model = Net().to(device)
    optimizer = torch.optim.Adadelta(model.parameters(), lr=1.0)

    # train_loader = torch_data.DataLoader( - ,batch_size=100, shuffle=False, **kwargs )
    # test_loader = torch_data.DataLoader( - ,batch_size=1000, shuffle=False, **kwargs )

    scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=1)
    for epoch in range(1, epochs + 1):
        # train(model, device, train_loader, optimizer, epoch)
        # test(model, device, test_loader)
        scheduler.step()


if __name__ == '__main__':
    main()
