# -*- mode: python ; coding: utf-8 -*-

import bookworm
from pathlib import Path


def get_datafiles():
    bwpath = Path(bookworm.__path__[0])
    res =  bwpath / "resources"
    rv = []
    wavs = res.rglob("*.wav")
    txts = res.rglob("*.txt")
    for collect in (wavs, txts):
        rv.extend([(str(f), str(f.relative_to(bwpath).parent)) for f in collect])
    return rv


block_cipher = None


a = Analysis(['launcher.py'],
             pathex=['C:\\Users\\ibnom\\app'],
             binaries=[],
             datas=get_datafiles(),
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Bookworm',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , version='artifacts\\version_info.txt', icon='artifacts\\bookworm.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Bookworm')
