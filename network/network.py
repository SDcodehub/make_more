import os
from pathlib import Path
import string
import torch
import torch.nn.functional as F


class NeuralNetwork:
    def __init__(self, lr, manual_seed) -> None:

        self.lr = lr
        chars = list(string.ascii_lowercase)
        chars.insert(0, '.')
        # string to index mapping we will call it as stoi
        self.stoi = {s:i for i,s in enumerate(chars)}
        self.itos = {i:s for s,i in self.stoi.items()}

        # For character level model, 26 character and +1 for start and end special character
        self.num_classes=27

        self.g = torch.Generator().manual_seed(manual_seed)

    def initialise_weights(self):
        # initialise the 'network'
        w = torch.randn((27,27), generator=self.g, requires_grad=True)
        return w

    def forward_pass(self, xs, w):
        # forward pass
        xenc = F.one_hot(xs, num_classes=self.num_classes).float() # input to the network one hot encodding
        logits = xenc @ w
        counts = logits.exp()
        probs = counts / counts.sum(1, keepdims=True)
        return probs

    def loss(self, probs, ys, num):

        loss = -probs[torch.arange(num), ys].log().mean()
        print(f'{loss.item()=}')
        return loss
    
    def backword_pass(self, loss, w):
        # backward pass
        w.grad = None
        loss.backward()
    
    def update_weights(self,w):
        # update
        w.data += -self.lr * w.grad

    def example_gen(self, words):
        xs, ys = [], []
        for w in words:
            chs = '.' + w+ '.'
            for ch1, ch2 in zip(chs, chs[1:]):
                ix1 = self.stoi[ch1]
                ix2 = self.stoi[ch2]
                xs.append(ix1)
                ys.append(ix2)
        xs = torch.tensor(xs)
        ys = torch.tensor(ys)
        num=xs.nelement()
        print(f'number of eaxmples: {num}')
        return xs, ys, num


if __name__ == '__main__':

    get_cwd = os.getcwd()
    project_dir = Path(get_cwd).parents[0]
    data_path = os.path.join(project_dir, 'data')
    words = open(os.path.join(data_path, "names.txt"), 'r').read().splitlines()

    nn = NeuralNetwork(1,2147483647)

    # Gen examples
    xs, ys, num = nn.example_gen(words)

    w = nn.initialise_weights()


    for k in range(500):

        # forward pass
        probs = nn.forward_pass(xs,w)

        # loss
        loss = nn.loss(probs, ys, num)

        # backward pass
        nn.backword_pass(loss, w)

        #update
        nn.update_weights(w)



