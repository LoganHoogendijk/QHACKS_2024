import torch
import torchvision.transforms as transforms
from PIL import Image
from .resnet9 import ResNet9, classes

class ImageClassifier():
    def __init__(self):
        self.classes = classes
        self.model_path = '.resnet9_model.pth'

    def load_model(self, path):
        resnet_model = torch.load(path)
        resnet_model.eval()
        loaded_model = resnet_model.to('cpu')
        return loaded_model

    def process_image(self, path):
        with Image.open(path) as img:
            resized_img = img.resize((256,256))
            transform = transforms.ToTensor()
            img_tensor = transform(resized_img)
        return img_tensor.unsqueeze(0)

    def predict(self, img_path):
        model = self.load_model(self.model_path)
        yb = model(self.process_image(img_path))
        _, preds  = torch.max(yb, dim=1)
        return classes[preds[0].item()]
    
    def result_dict(self, img_path):
        prediction = self.predict(img_path)
        result_dict = {'Plant Type': prediction.split('___')[0],
                       'Disease': prediction.split('___')[1],
                       'Healthy': int('healthy' in prediction.lower())}
        return result_dict
    
classifier = ImageClassifier()
print(classifier.result_dict('Tomato_EarlyBlight.jpg'))