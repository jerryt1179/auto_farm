# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['auto_farm.py'],
    pathex=[],
    binaries=[
        ('env/Lib/site-packages/vgamepad/win/vigem/client/x64/ViGEmClient.dll',
         'vgamepad/win/vigem/client/x64')
    ],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='auto_farm',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)