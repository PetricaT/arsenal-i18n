from pathlib import Path
from PIL import Image
import os

ROOT: Path = Path(__file__.split('scripts')[0] + "/locales")
LOCALES: list[str] = os.listdir(ROOT)
# MasOS is so annoying for this one
LOCALES.remove(".DS_Store")
ARSENAL_SIZE = (64, 64)

for LOCALE in LOCALES:
    _flag_path: Path = ROOT.joinpath(LOCALE + '/flag.png')
    if os.path.isfile(_flag_path):
        with Image.open(_flag_path) as _flag:
            if _flag.size != ARSENAL_SIZE:
                _flag = _flag.resize(ARSENAL_SIZE, Image.Resampling.LANCZOS)
                _flag.save(_flag_path, "PNG")

                print(f'Resized {LOCALE}/flag.png')