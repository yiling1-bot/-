import tkinter as tk
from tkinter import ttk
from PIL import ImageGrab
import os

class DesktopAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("桌面助手")
        self.root.geometry("800x600")
        
        # 创建界面
        self.create_widgets()
        
    def create_widgets(self):
        # 主界面
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 显示区域
        self.display_area = tk.Text(self.main_frame, wrap=tk.WORD)
        self.display_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 功能按钮
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.screenshot_btn = ttk.Button(self.button_frame, text="截屏", command=self.take_screenshot)
        self.screenshot_btn.pack(side=tk.LEFT, padx=5)
        
    def take_screenshot(self):
        # 获取屏幕截图
        screenshot = ImageGrab.grab()
        
        # 保存截图
        screenshot_dir = os.path.join(os.path.expanduser("~"), "Desktop", "Screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)
        
        screenshot_path = os.path.join(screenshot_dir, f"screenshot_{len(os.listdir(screenshot_dir)) + 1}.png")
        screenshot.save(screenshot_path)
        
        self.display_area.insert(tk.END, f"截图已保存到：{screenshot_path}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = DesktopAssistant(root)
    root.mainloop()
