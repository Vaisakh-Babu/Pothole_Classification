# Pothole_Classification  

### Problem Statement  
For a given image of a road, classify whether it contains potholes or not. 

### Data
Arround 700 images were taken from https://www.kaggle.com/atulyakumar98/pothole-detection-dataset and More than 300 images were taken using Mobile Camera(16 MegaPixel). Images with potholes and without potholes are in equal ratio. 

### Approach
preprocessing module from Keras is used to load and scale the images into same size(64,64,3). A neural network with 2 convolutional layers and Maxpooling layers are used to extract the feature from the images and a fully connected layer with 128 neurons are used before the output layer. 
The model gave 88% accuracy on the test dataset(train-test split = 90:10).
