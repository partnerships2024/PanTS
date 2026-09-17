<p align="center">
  <img
    src="./Logo/PanTS-Logo.png"
    alt="Pancreatic Tumor Segmentation Research" 
    width="700"
  />
</p>

# Pancreatic Tumor Segmentation Reproduction Pilot

## Task
Reproduction of a pancreatic tumor segmentation pipeline following the PanTS reproduction guidance.

## Dataset
Accessible Kaggle pancreatic cancer segmentation dataset.

Pilot subset:
- Training cases: 300
- Test cases: 50
- Seed: 42

This is a small pilot and is **not** the official PanTS-tr/PanTS-te benchmark.

## Model
nnU-Net v2, 2D configuration.

## Training
- Epochs: 5
- Fold: 0
- GPUs: 1
- Checkpoint: /kaggle/working/nnUNet_results/Dataset001_PancreaticTumorPilot/nnUNetTrainer_5epochs__nnUNetPlans__2d/fold_0/checkpoint_best.pth

## Testing metrics
Dice, IoU, precision, recall and HD95.

## Output files
- `checkpoint_best.pth` — trained pilot checkpoint
- `test.py` — testing/evaluation script
- `pilot_test_metrics.csv` — per-case metrics
- `pilot_summary_metrics.csv` — mean metrics
- `predictions/` — test predictions

## PanTS reference
https://github.com/MrGiovanni/PanTS

The official repository describes PanTS-tr (9,000 cases), PanTS-te (901 cases), and a full data download requiring about 300 GB. This pilot uses a smaller accessible dataset because the full dataset is not practical for this reproduction run.

