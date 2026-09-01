import subprocess
import sys
from pathlib import Path


PACKAGE_DIR = Path(__file__).parent

def render_animation():
    subprocess.run(
        [
            sys.executable,
            "-m",
            "manim",
            "-pqh",
            str(PACKAGE_DIR / "useful_derivatives.py"),
            "Derivatives",
        ],
        check=True,
    )

def render_picture():
    subprocess.run(
        [
            sys.executable,
            "-m",
            "manim",
            "-pqh",
            str(PACKAGE_DIR / "derivatives_simple.py"),
            "Derivatives",
        ],
        check=True,
    )