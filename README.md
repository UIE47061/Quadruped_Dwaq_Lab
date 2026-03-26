# Quadruped & Humanoid DWAQ Lab

本專案在 NVIDIA Isaac Lab 中實現了 **DWAQ (Deep Variational Autoencoder for Walking)** 演算法，用於四足機器人和人形機器人的穩健運動控制。

## 概述 (Overview)

**DWAQ** 利用 $\beta$-VAE 從觀測歷史中學習潛在表示 (Latent Representation)，透過估計速度並編碼隱含的環境特徵，實現盲走 (Blind Walking) 能力。

### 參考 (Acknowledgements & References)
本專案基於 [G1DWAQ_Lab](https://github.com/liuyufei-nubot/G1DWAQ_Lab?tab=readme-ov-file) 進行開發，將原有的 G1 人形機器人訓練擴展至 Go2 及其他四足機器人。

- **算法復現**: 本項目在 IsaacLab 中復現 DreamWaQ 算法，DreamWaQ 算法部分參考了 [Manaro-Alpha](https://github.com/Manaro-Alpha)。
- **框架基礎**: 整體框架基於 [天工 TienKung-Lab](https://github.com/TienKung-Lab) 和 [Legged Lab](https://github.com/LeggedRobotics/LeggedLab) 開源框架。


### 主要功能 (Key Features)
- **演算法**: DWAQ (Deep Variational Autoencoder for Walking)
- **框架**: 基於 [Isaac Lab](https://github.com/isaac-sim/IsaacLab) 構建
- **核心函式庫**: [TienKung-Lab](TienKung-Lab/)

## 支援的機器人 (Supported Robots)
基於現有的配置和實驗：
- **四足機器人 (Quadrupeds)**:
  - Unitree Go2 (`go2_dwaq`)
  - Big Red Dog (`bigreddog_dwaq`)
  - Little White (`little_white_dwaq`)

## DWAQ 架構 (DWAQ Architecture)
DWAQ 潛在編碼 (Latent Code) 由一個 19 維向量組成：
- **速度 (Velocity, 3 維)**: 監督式學習 (MSE)，用於估計機器人速度。
- **潛在狀態 (Latent State, 16 維)**: 非監督式學習 ($\beta$-VAE)，用於編碼隱含的環境特徵。

更多詳細資訊，請參閱 [DWAQ 分析](TienKung-Lab/docs/DWAQ_LATENT_CODE.md)。

## 安裝指南 (Installation)

1. **先決條件 (Prerequisites)**:
   - NVIDIA Isaac Sim 4.5.0
   - Isaac Lab 2.1.0

2. **設定 (Setup)**:
   複製 (Clone) 此儲存庫：
   ```bash
   git clone https://github.com/your-username/Quadruped_Dwaq_Lab.git
   cd Quadruped_Dwaq_Lab
   ```

   在您的 Python 環境中安裝依賴項（請確保已安裝 Isaac Lab）：
   ```bash
   cd TienKung-Lab
   pip install -e .
   ```

## 使用方法 (Usage)

請參考 `TienKung-Lab` 中的腳本進行訓練和部署。

### 訓練 (Training)
```bash
cd TienKung-Lab
# 執行訓練腳本（請查看腳本中的參數）
./train_play.sh
```

## 目錄結構 (Directory Structure)
- `IsaacLab/`: 核心模擬框架 (submodule 或副本)。
- `TienKung-Lab/`: 主要的 DWAQ 實作，結合了 RSL_RL 和 Isaac Lab 環境。
- `docs/`: DWAQ 演算法的文件。
