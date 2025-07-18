import os
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Final PC Build Summary for ML + Gaming (with Prices)", ln=True, align="C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 8, body)
        self.ln()

components = """
Core PC Components:
- CPU: Intel Core i5-13600K - Rs. 24,337
- GPU: MSI Geforce RTX 5070  12G Gaming Trio OC - Rs. 88,000
- Cooler: CORSAIR Nautilus 360 RS  - Rs. 9,000
- Motherboard: GIGABYTE Z790 AORUS Elite AX - Rs. 18,500
- RAM: CORSAIR Vengeance DDR5 32GB (2x16GB) 6000MHz CL36 - Rs. 10,629
- SSD: WD Black SN770 2TB - Rs. 12,500
- PSU: MSI MAG A850GL PCIe 5.1, 850W, 80+ Gold - Rs. 9,750
- Case: NZXT H6 Flow Black  - Rs. 10,000
- Fans: Corsair RX 120 RGB  - Rs. 2,400
Total (Approx): Rs. 188,000
"""

accessories = """
Additional Notes:
- External SSD: Samsung 2TB External SSD (used with MacBook Air M1)
- OS: Windows 11 Pro or Dual Boot with Ubuntu/Pop!_OS
- Software: Python, Docker, Git, VSCode, Anaconda
- ML Frameworks: PyTorch, TensorFlow, CUDA Toolkit, cuDNN

Dropped from original list (to save cost):
- Monitor (was ~Rs. 13,000)
- Moondrop Chu II IEMs (was ~Rs. 2,000)
"""

# Path to Downloads folder
downloads_path = os.path.expanduser("~/Downloads/RTX_4070_PC_Build_Bibhanshu.pdf")

# Generate and save PDF
pdf = PDF()
pdf.add_page()
pdf.chapter_title("1. Components with Prices")
pdf.chapter_body(components)
pdf.chapter_title("2. Notes and Software Setup")
pdf.chapter_body(accessories)
pdf.output(downloads_path)

print(f"PDF saved to: {downloads_path}")
