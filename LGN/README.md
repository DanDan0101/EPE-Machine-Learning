# LGN

Read the Lorentz Group Network [paper](https://arxiv.org/abs/2006.04780) and [repo](https://github.com/fizisist/LorentzGroupNetwork). This implementation requires a GPU to train.

## Overview of the repository

**zenodo**: Raw top tagging data files from the [Top Quark Tagging Reference Dataset](https://zenodo.org/record/2603256)

**converted**: Converted data files according to LGN specification

**run**: Logs, model, and ROCs generated by `train_lgn.py`. ROC curves generated by `figures/scripts/build_roc_curves.py`

**figures**: Scripts to generate ROC curves, epoch time summaries, and performance plots

**summary/plt**: Output from `figures/scripts/perf_plot.py`

### Package dependencies
- Python3
- h5py
- numba
- numpy
- pandas
- cudatoolkit
- h5py
- PyTorch
- torchvision

## Installing LGN

1. Clone the [LGN repository](https://github.com/fizisist/LorentzGroupNetwork) to your local machine.
2. Create a conda environment and install necessary packages:
```bash
conda create -n pt python=3.7 anaconda
conda activate pt
conda install pytorch torchvision cudatoolkit=10.0 -c pytorch
```
Note that the wrong version of PyTorch will be installed if the `-c pytorch` option is omitted from `conda install pytorch`.

3. Navigate to the LGN repository directory and run `pip install -e .`

## Dataset conversion
See `fileformats.ipynb` notebook to understand the format of the raw `zenodo` datasets as well as the format of the `converted` datasets.

`convert.ipynb` is used to generate converted dataset from raw `zenodo` dataset.

## Training and evaluation

The model is trained through the command line using `train_lgn.py`. Navigate to the project directory and run the following command: `python ./train_lgn.py --datadir=converted --num-epoch=1 --batch-size=2`

- Depending on how much memory your GPU has, you can increase the batch size.
- Depending on how much time you have and how powerful your GPU is, you can increase the number of epochs.

## Printing epoch time

Navigate to `figures/scripts` and run `python ./epoch_time.py ../../`

On a GTX 960 GPU, training 1 epoch took 67.74 hours, with 8.28 hours of evaluation on the validation set and 8.53 hours of evaluation on the test set.

## Drawing ROC curves

Navigate to `figures/ROC_curves` and run:
```bash
python ./buildTopTagROC.py ../../run/predict/nosave.best.test_ROC.csv light ./TopTagReference/ ../../run/ROCcomparisons/ ROCcomparisons 1 ../../zenodo/test.h5
```

If you've trained more than 1 epoch, you can draw performance plots. Navigate to `figures/scripts` and run (replace [number of epochs] with the number of epochs you've trained)
```bash
python ./perf_plot.py ../../ 1 1 perf_plot [number of epochs]
```