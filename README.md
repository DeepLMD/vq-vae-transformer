# VQ-Transformer Framework

This repository is based on the **Sparse-VQ Transformer** framework and provides implementations of various **VQ** methods and **Linear Models**.
Each method and model is organized in its own branch to allow for straightforward experimentation and performance evaluation.

## Available VQ Methods and Branches

To access and use a specific VQ method or linear model, switch to the branch associated with that method.
The branches follow this naming convention:

main-[vq-method-placeholder]-exp


### VQ Methods

Here are the VQ methods currently available and their corresponding branch names:

| VQ Method                          | Branch Name                  |
|------------------------------------|------------------------------|
| Vanilla VQ                         | `main-vanilla-vq-exp`        |
| Without VQ                         | `main-svq0-exp`              |
| RLFQ                               | `main-residual-lfq-exp`      |
| GRVQ                               | `main-grvq-exp`              |
| LFQ                                | `main-LFQ-exp`               |
| RFSQ                               | `main-residual-fsq-exp` |
| RVQ                                | `main-rvq-exp`               |

### Linear Models

| Linear Model       | Branch Name                  |
|--------------------|------------------------------|
| LTSF-Linear        | `main-LTSF-Linear-exp`       |


## Datasets

The raw datasets used in this framework can be accessed through the following sources:

- **Traffic Dataset**: The raw traffic dataset is available at the [PeMS website](http://pems.dot.ca.gov).
- **Electricity Dataset**: The raw electricity dataset is available at the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/321/electricityloaddiagrams20112014).


## Acknowledgement

Appreciation goes to the following repositories for their valuable code bases and datasets:

https://github.com/yuqinie98/PatchTST

https://github.com/MAZiqing/FEDformer

https://github.com/lucidrains/vector-quantize-pytorch

https://github.com/Yanjun-Zhao/Sparse-VQ

https://github.com/Pachark/SVQ-Forecasting

