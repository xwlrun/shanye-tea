"""生成本站二维码：python tools/make_qr.py <网址>
依赖 segno（纯 Python，无需系统库）：pip install segno
"""
import sys
from pathlib import Path

import segno

url = sys.argv[1] if len(sys.argv) > 1 else "https://example.github.io/linxiaozhou/"
out = Path(__file__).resolve().parent.parent / "assets" / "qr.png"
out.parent.mkdir(parents=True, exist_ok=True)
segno.make(url, error="m").save(str(out), scale=8, border=2, dark="#0f4c81", light="#fbfaf7")
print(f"二维码已生成：{out}（内容：{url}）")
