# Convolutional Neural Networks

<!-- LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Yashvardhang/CNN">
    <img src="Icons/CNN.svg" alt="Logo" width="128" height="128">
  </a>
  <h3 align="center">CNN</h3>
  <p align="center">
   Convolutional Neural Network Projects
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about">About</a></li>
    <li><a href="#requirements">Requirements</a></li>
    <li><a href="#projects">Projects</a>
      <ul>
        <li><a href="#recognition">Image Recognition Software</a></li>
      </ul>
    </li>
    <li><a href="#working">Working</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contribute">Contribute</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT -->
## About

Neural networks reflect the behavior of the human brain, allowing computer programs to recognize patterns and solve common problems in the fields of AI, machine learning, and deep learning. Artificial neural networks (ANNs) are comprised of a node layers, containing an input layer, one or more hidden layers, and an output layer. Each node, or artificial neuron, connects to another and has an associated weight and threshold. If the output of any individual node is above the specified threshold value, that node is activated, sending data to the next layer of the network. Otherwise, no data is passed along to the next layer of the network.

A **Convolutional Neural Network** (CNN/ConvNet) is, a class of neural networks that specializes in processing data that has a grid-like topology, such as an image. A digital image is a binary representation of visual data. It contains a series of pixels arranged in a grid-like fashion that contains pixel values to denote how bright and what color each pixel should be.

This project consists of various examples of Convolutional Neural Networks developed using <a href = 'https://www.tensorflow.org/'> Tensorflow </a> which is integrated in the **Python** programming language.

You may head on the the <a href="#projects">Projects</a> section to view all the CNN models developed.

Since Tensorflow has been integrated in the Python Programming language, it requires some modules to operate. The list of required modules and installation commands have been given in the <a href="#requirements">next</a> section.

<!-- REQUIREMENTS -->
## Requirements

It is advisable if you upgrade your pip version because some modules might require the latest version of pip. To upgrade your pip, run the following command in your command prompt.

```
 > pip install --upgrade pip
```

Here is the main pre-requisite modules required to run the ConvNet projects.

```
 > pip install tensorflow
 > pip install keras
 > pip install matplotlib
 > pip install numpy
 > pip install tk
```

**Note:** All of these modules might not be required to run each project. Each project requires different modules, and you may head on to the specific project in order to know more about it.

<!-- PROJECTS -->
## Projects

Here are some ConvNet sample projects:

### Recognition

<br><br>
<p align="center">
  <img src = "Icons/Image.svg" width="128" height="128">
</p>

This Image Recognition/Classification Software is built using the **CIFAR-10 Dataset** (Canadian Institute for Advanced Research, 10 Classes). The CIFAR-10 dataset consists of 60000 32x32 colour images in 10 classes, with 6000 images per class. There are 50000 training images and 10000 test images. <br>

The dataset is divided into five training batches and one test batch, each with 10000 images. The test batch contains exactly 1000 randomly-selected images from each class. The training batches contain the remaining images in random order, but some training batches may contain more images from one class than another. Between them, the training batches contain exactly 5000 images from each class.<br>

You may head on to <a href = 'https://github.com/YashvardhanG/CNN/tree/main/Image%20Recognition%20Software'>Image Recognition</a> to explore and know more about the project.

**Note:** The dataset is downloaded as soon as you open the main code, but you may also download the CIFAR-10 Dataset Externally. To download the CIFAR-10 Dataset, head on to <a href = 'https://www.cs.toronto.edu/~kriz/cifar.html'>CIFAR-10</a> website.
<br><br>

<!-- WORKING -->
## Working

You may explore the working of a Convolutional Neural Network <a href = 'https://towardsdatascience.com/convolutional-neural-network-17fb77e76c05#:~:text=Fully%20Connected%20Layer%20is%20simply,into%20the%20fully%20connected%20layer.'>Here</a>.
<br><br>
The working of all the projects can broadly be categorised into two steps:
<ol>
  <li><b>Training:</b><br>This is the initialising step, or can be considered as the pre-processing step of a ConvNet. This indeed is the most important steop because this is where the CNN actually learns and understands the purpose of the user-application, and compiles a data model which can be integrated in a main driver code/application. This is the primary step where data is sorted, analysed, processed and arranged. </li><br>
  <li><b>Testing:</b><br>This is the secondary step of a CNN which includes the usage of the created data model in the previous step. In this step, you will create the driver code/application which will provide a user interface to interact with the dataset in order to carry out a specific operation, for which the application is designed for. This in summary, is the 'fancy' of a CNN.</li><br>
</ol>

To know more about the working of different projects, go ahead and explore all the <a href="#projects">Projects</a>.
<br>
**Note:** Each CNN is different, and you may or may not put both of these steps in the same code.
<br><br>

<!-- LICENSE -->
## License

Distributed under the MIT License. See <a href = "https://github.com/YashvardhanG/CNN/blob/main/LICENSE"> LICENSE </a> for more information.

<!-- contribute -->
## Contribute

Every program is ever evolving and, that is possible only with valuable contributions. Any contributions you make are greatly appreciated. 
<ol>
  <li>Fork the Project</li>
  <li>Create your Feature Branch (git checkout -b functionalities/Feature)</li>
  <li>Commit your Changes (git commit -m 'Add a Feature')</li>
  <li>Push to the Branch (git push origin functionalities/Feature)</li>
  <li>Open a Pull Request</li>
</ol>

<br>If you have any further ideas or comments, go ahead to the next section and feel free to connect! 

<!-- CONTACT -->
## Contact

<p align="center">
  <br>
  <img src="https://github.com/YashvardhanG/YashvardhanG/blob/main/Spiral%20Cosmos.png" alt="Logo" width="155" height="140"><br><br>
  <a href = "https://www.spiralcosmos.com">Spiral Cosmos</a>
</p>

<!-- Acknowledgement -->
## Acknowledgements

<ul>
  <li><a href = 'https://www.ibm.com/cloud/learn/neural-networks'>Neural Networks</a></li>
  <li><a href = 'https://towardsdatascience.com/convolutional-neural-networks-explained-9cc5188c4939#:~:text=A%20Convolutional%20Neural%20Network%2C%20also,topology%2C%20such%20as%20an%20image.&text=Each%20neuron%20works%20in%20its,cover%20the%20entire%20visual%20field.'>Convolutional Neural Networks</a></li>
  <li><a href = 'https://towardsdatascience.com/convolutional-neural-network-17fb77e76c05#:~:text=Fully%20Connected%20Layer%20is%20simply,into%20the%20fully%20connected%20layer.'>Working of CNN</a></li>
  <li><a href = 'https://developers.google.com/machine-learning/glossary/#convolutional_neural_network'>CNN Glossary</a></li>
  <li><a href = 'https://www.flaticon.com/'>Icons</a></li>
</ul>

