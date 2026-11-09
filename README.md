# 人脸表情分类

这个项目使用 ResNet34、EfficientNet-B0 和 EfficientNet-B2 识别 6 类人脸表情，训练和预测在 Kaggle Notebook 中完成。

## 代码文件

| 文件 | 用途 |
| --- | --- |
| `cell_01_write_training_module.txt` | 定义数据处理、模型、五折训练和预测，并写成 Python 脚本 |
| `cell_02_run_training.py` | 启动训练脚本并显示日志 |

## 在 Kaggle 上运行

1. 在 Kaggle Notebook 中添加比赛数据并启用 GPU。
2. 确认环境包含 PyTorch、timm、NumPy、pandas、OpenCV、scikit-learn 和 Albumentations。首次下载 ImageNet 预训练权重时需要允许联网。
3. 将两个文件分别复制到同一个 Notebook 的两个代码单元格，按 `01`、`02` 的顺序运行。保留第一个单元格首行的 `%%writefile`，第二个单元格会运行它写出的脚本。
4. 运行完成后，在 `/kaggle/working/submission.csv` 查看预测结果。文件含 `ID` 和 `Emotion` 两列。
