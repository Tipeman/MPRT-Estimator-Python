# MPRT 估算器 (MPRT Estimator)

这是一个基于 Python 和 Tkinter 的轻量级桌面应用程序，用于估算液晶显示器（LCD）的**运动图像响应时间 (MPRT)**。

MPRT 是衡量显示器在显示快速运动画面时的清晰度的关键指标，它同时考虑了像素转换速度和画面保持时间。

## 🔬 估算公式

本工具使用的 MPRT 估算公式结合了平均 GtG 响应时间和刷新周期，以**均方根 (RMS)** 的形式计算实际感知到的运动模糊程度。

$$
\text{MPRT} \approx \sqrt{(\text{平均 GtG 响应时间})^{2} + \left( 0.8 \times \frac{1000}{\text{刷新率}} \right)^{2}}
$$

* **$\text{平均 GtG 响应时间}$ (ms)：** 像素颜色转换所需的时间（影响拖影）。
* **$\frac{1000}{\text{刷新率}}$ (ms)：** 刷新周期，即画面保持不变的时间（影响动态模糊）。
* **$0.8$：** 经验修正系数。

## ✨ 特性

* **简洁 UI：** 基于 Python 内置的 `tkinter` 库，界面简洁，易于操作。
* **科学估算：** 结合 GtG 和刷新率，提供更贴近实际感知的 MPRT 估算值。
* **独立运行：** 纯 Python 标准库编写，环境配置简单。

## 🚀 如何运行

### 前提条件

您需要安装 [Python 3.x](https://www.python.org/downloads/) 环境。

### 运行步骤

1.  **下载代码：** 克隆本仓库或直接下载 `mprt_calculator.py` 文件。
    ```bash
    git clone [https://github.com/Tipeman/MPRT-Estimator-Python.git](https://github.com/Tipeman/MPRT-Estimator-Python.git)
    cd MPRT-Estimator-Python
    ```
2.  **执行脚本：** 在命令行中运行 Python 文件。
    ```bash
    python mprt_calculator.py
    ```

### 使用方法

1.  在 **"平均 GtG 响应时间 (ms)"** 框中输入显示器的 GtG 值（例如：`4.0`）。
2.  在 **"刷新率 (Hz)"** 框中输入显示器的刷新率（例如：`144`）。
3.  点击 **"计算 MPRT"** 按钮，结果将实时显示。

## 🤝 贡献

欢迎任何形式的贡献和改进建议！如果您发现任何 bug 或有更好的功能建议，请随时提交 Issue 或 Pull Request。

## 许可证

本项目遵循 [MIT 许可证](LICENSE) 发布。