"""
Music analysis and genre-classification using a python feed forward NN
"""
from NeuralNetwork.NeuralNetwork import NeuralNetwork
import numpy as np


if __name__ == "__main__":
    network = NeuralNetwork([2, 5, 5, 1])
    print(network.feed_forward(np.transpose(np.array([[0, 0]])))[-1])
    print(network.feed_forward(np.transpose(np.array([[1, 0]])))[-1])
    print(network.feed_forward(np.transpose(np.array([[0, 1]])))[-1])
    print(network.feed_forward(np.transpose(np.array([[1, 1]])))[-1])
    inputs = [[[[1, 0]], [1]], [[[0, 1]], [1]], [[[1, 1]], [1]], [[[0, 0]], [0]]]