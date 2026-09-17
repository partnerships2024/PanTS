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

## Motivation

Our pancreatic tumour segmentation research is motivated by recent advances in **medical image segmentation, AI-driven radiology, and reproducible open-source research**. The following resources provide key methodological, scientific, and implementation foundations for this work.

| **Researcher / Resource** | **Research Papers & Open-Source Implementations** |
|:---|:---|
| **Prof. Dr. Zongwei Zhou** | [Website](https://www.zongweiz.com) · [PanTS GitHub Repository](https://github.com/MrGiovanni/PanTS) |
| **Relevant Research Papers** | [Paper 1](https://arxiv.org/abs/2507.01291) · [Paper 2](https://arxiv.org/abs/1912.05074) · [Paper 3](https://arxiv.org/abs/2102.04306) · [Paper 4](https://arxiv.org/abs/2203.00131) · [Paper 5](https://arxiv.org/html/2604.20981v1) |

### Key Reference: Learning Segmentation from Radiology Reports

**Learning Segmentation from Radiology Reports**  
Pedro R. A. S. Bassi, Wenxuan Li, Jieneng Chen, Zheren Zhu, Tianyu Lin, Sergio Decherchi, Andrea Cavalli, Kang Wang, Yang Yang, Alan Yuille, and Zongwei Zhou.  

**Johns Hopkins University** · **MICCAI 2025 — Best Paper Award (Runner-up)**

**Research & Implementation Resources**

[![Paper](https://img.shields.io/badge/Paper-PDF-purple?style=for-the-badge)](https://www.cs.jhu.edu/~zongwei/publication/bassi2025learning.pdf)
[![Poster](https://img.shields.io/badge/Poster-PDF-blue?style=for-the-badge)](https://www.cs.jhu.edu/~zongwei/poster/bassi2025miccai_rsuper.pdf)
[![JHU News](https://img.shields.io/badge/JHU-News-green?style=for-the-badge)](https://www.cs.jhu.edu/news/for-ai-tumor-detection-a-picture-isnt-always-worth-a-thousand-words/)
[![YouTube](https://badges.aleen42.com/src/youtube.svg)](https://youtu.be/7pamG9DDSJw?si=-376z03g832UyTKB)
[![Oral Presentation](https://img.shields.io/badge/Oral-RSNA-orange?style=for-the-badge)](https://youtu.be/r11X39fH-yU?si=ZOBlHMo1CvN9aVzb)

### Why This Work Matters

These resources provide a foundation for developing **reproducible pancreatic tumour segmentation pipelines**, combining published medical imaging methods with publicly available implementations. Our work builds upon these foundations while focusing on **reproduction, validation, and further development of AI-based pancreatic tumour segmentation methods**.

# CHI Lab Research

[![CHI Lab](https://img.shields.io/badge/CHI%20Lab-Research-0A7EA4?style=for-the-badge)](https://icriste.com/computational-healthcare-intelligence-lab-chi-lab/)
[![ICRI-STE Website](https://img.shields.io/badge/Website-ICRI--STE-00A6A6?style=for-the-badge&logo=googlechrome&logoColor=white)](https://icriste.com)


This project forms part of the CHI Lab's computational healthcare and cancer research activities, integrating **Systems-Oriented Computational Research, Artificial Intelligence/Deep Learning, and Virtual Lab for AI-Driven Agentic System**.

| CHI Lab Repository | Access |
|:---|:---|
| **CHI Lab — Public Repository Research Direction on Pancreatic Cancer** | [![GitHub](https://img.shields.io/badge/GitHub-Open%20Science-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/partnerships2024/CHI-Lab-Research-Pancreatic-Cancer.git) |


---
<div align="center">
<img src="./Logo/CHI-Lab.png" alt="Computational Healthcare Intelligence Lab (CHI Lab)" width="120"/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src="./Logo/ICRI-STE.png" alt="International Council for Research & Innovation in STE (ICRI-STE)" width="120"/>
  
**CHI Lab | Computational Healthcare Intelligence | Dry Lab**

**International Council for Research & Innovation in STE (ICRI-STE)**

*From Pancreatic Cancer Segmentation to Computational Intelligence*
