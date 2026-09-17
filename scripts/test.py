
import os, argparse
from pathlib import Path
import cv2, nibabel as nib
import numpy as np
import pandas as pd

def dice(gt, pred):
    gt, pred = gt.astype(bool), pred.astype(bool)
    d = gt.sum() + pred.sum()
    return 1.0 if d == 0 else 2*np.logical_and(gt,pred).sum()/d

def iou(gt, pred):
    gt, pred = gt.astype(bool), pred.astype(bool)
    u = np.logical_or(gt,pred).sum()
    return 1.0 if u == 0 else np.logical_and(gt,pred).sum()/u

def edt_from_mask(mask):
    src = np.where(mask, 0, 255).astype(np.uint8)
    return cv2.distanceTransform(src, cv2.DIST_L2, 5)

def get_surface(mask):
    m = mask.astype(np.uint8)
    kernel = np.ones((3, 3), np.uint8)
    eroded = cv2.erode(m, kernel, iterations=1)
    return m.astype(bool) ^ eroded.astype(bool)

def hd95(gt, pred):
    gt, pred = gt.astype(bool), pred.astype(bool)
    if not gt.any() and not pred.any(): return 0.0
    if not gt.any() or not pred.any(): return np.nan
    gs = get_surface(gt)
    ps = get_surface(pred)
    d1 = edt_from_mask(pred)[gs]
    d2 = edt_from_mask(gt)[ps]
    return float(np.percentile(np.concatenate([d1,d2]),95))

ap = argparse.ArgumentParser()
ap.add_argument("--images", required=True)
ap.add_argument("--masks", required=True)
ap.add_argument("--predictions", required=True)
ap.add_argument("--output", default="test_metrics.csv")
args = ap.parse_args()

rows=[]
for img_name in sorted(os.listdir(args.images)):
    if not img_name.endswith(".png"): continue
    mask_name = img_name.replace(".png","_modified.png")
    pred_name = img_name.replace(".png",".nii.gz")
    gt = cv2.imread(str(Path(args.masks)/mask_name), cv2.IMREAD_GRAYSCALE) > 0
    pred = np.asarray(nib.load(str(Path(args.predictions)/pred_name)).get_fdata()) > 0
    rows.append({
        "case": img_name,
        "dice": dice(gt,pred),
        "iou": iou(gt,pred),
        "hd95": hd95(gt,pred)
    })

df=pd.DataFrame(rows)
df.to_csv(args.output,index=False)
print(df)
print("\nMean metrics:")
print(df[["dice","iou","hd95"]].mean())
