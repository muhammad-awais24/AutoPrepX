# ⚡ AutoPrepX: Smart Parallel Data Preprocessing Engine

AutoPrepX is a high-performance, modular data preprocessing platform designed to accelerate machine learning pipelines. By leveraging parallel execution (concurrent multiprocessing), it slashes compute times compared to standard sequential cleaning pipelines.

## 🚀 Key Features
* **Parallel Orchestration (`engine.py`):** Efficiently dispatches concurrent workers to clean data.
* **Modular Preprocessing:**
  * `missing.py`: Fast statistical median imputation.
  * `outliers.py`: Outlier detection using the Interquartile Range (IQR) method.
  * `encoding.py`: Explicit, robust protection of critical text/categorical data.
  * `scaling.py`: Mathematical normalization of continuous targets.
* **Real-time Animated Dashboard:** Futuristic glassmorphism UI showing pipeline execution pathways and performance gains.

## 🛠️ Built With
* Python (Multiprocessing & Pandas)
* Streamlit (App wrapper)
* Modern CSS & SVG Animations (Interactive pipeline dashboard)
