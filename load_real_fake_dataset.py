import os
import torch
from torch.utils.data import Dataset
from PIL import Image
from torchvision import transforms

class RealFakeDataset(Dataset):
    def __init__(self, root_dir):
        self.data = []
        self.transform = transforms.Compose([
            transforms.Resize((128, 128)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.5]*3, std=[0.5]*3)
        ])
        
        for label, subfolder in enumerate(['fake', 'real']):
            class_path = os.path.join(root_dir, subfolder)
            for fname in os.listdir(class_path):
                if fname.lower().endswith(('.jpg')):
                    self.data.append((os.path.join(class_path, fname), label))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        img_path, label = self.data[idx]
        image = Image.open(img_path).convert('RGB')
        image = self.transform(image)
        return image, torch.tensor(label, dtype=torch.long)
