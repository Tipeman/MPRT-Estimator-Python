import tkinter as tk
from tkinter import ttk, messagebox
import math

# --- MPRT 估算公式函数 ---
def calculate_mprt(gtg_ms, refresh_rate_hz):
    """
    根据均方根公式估算 MPRT：
    MPRT ≈ sqrt( (平均 GtG 响应时间)² + (0.8 * 1000 / 刷新率)² )
    """
    try:
        # 1. 计算刷新周期项（毫秒）
        refresh_term_ms = 0.8 * (1000 / refresh_rate_hz)
        
        # 2. 应用均方根公式
        mprt_ms = math.sqrt(gtg_ms**2 + refresh_term_ms**2)
        
        return mprt_ms
        
    except ZeroDivisionError:
        # 刷新率不能为 0
        return None
    except Exception:
        # 其他异常，如输入非数字等
        return None

# --- UI 逻辑函数 ---
def calculate_and_display():
    """获取输入，执行计算，并显示结果。"""
    try:
        # 1. 获取输入并转换为浮点数
        gtg_input = entry_gtg.get()
        refresh_input = entry_refresh.get()

        # 检查输入是否为空
        if not gtg_input or not refresh_input:
            messagebox.showwarning("输入错误", "请确保所有输入字段都已填写。")
            return

        gtg_ms = float(gtg_input)
        refresh_rate_hz = float(refresh_input)

        # 检查输入是否有效（GtG和刷新率应大于0）
        if gtg_ms <= 0 or refresh_rate_hz <= 0:
            messagebox.showwarning("输入错误", "GtG和刷新率必须是正数。")
            return
            
    except ValueError:
        messagebox.showerror("输入错误", "请在输入框中输入有效的数字。")
        return

    # 2. 执行计算
    mprt_result = calculate_mprt(gtg_ms, refresh_rate_hz)
    
    # 3. 显示结果
    if mprt_result is not None:
        result_text = f"{mprt_result:.2f} ms"
        label_result.config(text=f"估算 MPRT: {result_text}", foreground="#00CC99")
    else:
        label_result.config(text="估算 MPRT: 计算失败", foreground="red")


# --- 界面设置 ---
app = tk.Tk()
app.title("MPRT 估算器")

# 设置主题和字体
style = ttk.Style()
style.configure("TLabel", font=("Microsoft YaHei", 10))
style.configure("TButton", font=("Microsoft YaHei", 10, "bold"))

# 主框架
frame = ttk.Frame(app, padding="20 20 20 20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# --- 1. 输入：平均 GtG 响应时间 ---
label_gtg = ttk.Label(frame, text="平均 GtG 响应时间 (ms):")
label_gtg.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

entry_gtg = ttk.Entry(frame, width=15)
entry_gtg.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
entry_gtg.insert(0, "4.0") # 默认值

# --- 2. 输入：刷新率 ---
label_refresh = ttk.Label(frame, text="刷新率 (Hz):")
label_refresh.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

entry_refresh = ttk.Entry(frame, width=15)
entry_refresh.grid(row=1, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
entry_refresh.insert(0, "144") # 默认值

# --- 3. 计算按钮 ---
button_calculate = ttk.Button(frame, text="计算 MPRT", command=calculate_and_display)
button_calculate.grid(row=2, column=0, columnspan=2, pady=15)

# --- 4. 结果显示 ---
label_result = ttk.Label(frame, text="估算 MPRT: N/A", font=("Microsoft YaHei", 12, "bold"))
label_result.grid(row=3, column=0, columnspan=2, pady=10)

# --- 5. 公式说明（可选） ---
formula_label = ttk.Label(
    frame, 
    text="基于公式: MPRT ≈ √[ GtG² + (0.8 × 1000/Hz)² ]",
    font=("Microsoft YaHei", 8),
    foreground="gray"
)
formula_label.grid(row=4, column=0, columnspan=2, pady=(10, 0))


# 运行应用
app.mainloop()