# EPE-Machine-Learning
A collection of my work done under the supervision of Professor Shih-Chieh Hsu at the University of Washington. We seek to deploy Deep Learning jet tagging algorithms into Reproducible Open Benchmarks (ROB) framework for automating performance evaluations of different models. We use modern data science tools and Machine Learning frameworks using LHC data.

Collaborative work on projects after October 2020 can be found at [Theory-Based-Networks](https://github.com/hmyin516/Theory-Based-Networks) and [AnomalyDetection](https://github.com/hmyin516/AnomalyDetection).

## Package Dependencies
- numpy
- pandas
- h5py
- matplotlib
- tensorflow >= 2.2
- tensorflow-gpu
- keras
- sklearn
- pytorch
- torchvision
- cudatoolkit

## Feature-Exploration
Sample code for feature exploration of Monte Carlo simulated dataset using Pythia. Both high level features and low level features are explored.

## LBN
Lorentz Boost Network, [paper](https://arxiv.org/abs/1812.09722) and [repo](https://github.com/riga/LBN). We trained the network using convert.ipynb and train.ipynb with the [Top Quark Tagging Reference Dataset](https://zenodo.org/record/2603256#.X1liUHlKguU).

## LGN
Lorentz Group Network, [paper](https://arxiv.org/abs/2006.04780) and [repo](https://github.com/fizisist/LorentzGroupNetwork). We trained the network using train_lgn.py with the [Top Quark Tagging Reference Dataset](https://zenodo.org/record/2603256#.X1liUHlKguU).

Currently this is the most complete and organized directory. See the [LGN readme](./LGN/README.md) for more information.
