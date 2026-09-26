#!/usr/bin/env python3

#this program takes a .MPG and converts to .WAV, so videos from Sony DCR-SR67 can be utilized for samples in logic pro

import subprocess
import sys
from pathlib import Path

def convert(folder: Path, output_format: str = "wav") -> None:
    files = sorted(f for f in folder.iterdir() if f.suffix.lower() == ".mpg")
    if not files:
        print(f"No .mpg files found in {folder}")
        return

    for f in files:
        out = f.with_suffix(f".{output_format}")
        print(f"Converting {f.name} -> {out.name}")
        subprocess.run(
            ["ffmpeg", "-y", "-i", str(f), "-vn", "-c:a", "pcm_s16le", str(out)],
            check=True,
        )

if __name__ == "__main__":
    folder = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    convert(folder)   
