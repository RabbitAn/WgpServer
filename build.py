import subprocess

# 自动检测编码
import chardet
with open("requirements.txt", "rb") as f:
    raw = f.read()
encoding = chardet.detect(raw)["encoding"]

# 按检测到的编码读取
packages = []
for line in raw.decode(encoding).splitlines():
    line = line.strip()
    if line and not line.startswith("#"):
        pkg = line.split("==")[0]
        packages.append(pkg)

# 构造 --collect-all 参数
collect_args = []
for pkg in packages:
    collect_args += ["--collect-all", pkg]

# 执行 PyInstaller
cmd = ["pyinstaller", "--onefile", "main.py", "--noconfirm", "--clean"] + collect_args
print("执行命令:", " ".join(cmd))
subprocess.run(cmd)
