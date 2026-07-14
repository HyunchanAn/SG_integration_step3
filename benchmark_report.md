# Benchmark & E2E Test Report

- **Repository**: SG_integration_step3
- **Date**: 2026-07-14 22:41:55

## 1. E2E Testing Summary
❌ **Status**: FAILED

### Test Logs (Snippet)
```text
collected 13 items / 1 error

==================================== ERRORS ====================================
___________ ERROR collecting SG_proj_009/tests/test_ir_simulator.py ____________
ImportError while importing test module '/Users/hyunchanan/Documents/GitHub/SG_integration_step3/SG_proj_009/tests/test_ir_simulator.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/homebrew/Caskroom/miniconda/base/lib/python3.13/importlib/__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SG_proj_009/tests/test_ir_simulator.py:4: in <module>
    from ir_simulator import generate_ir_spectrum, optimize_mixture_ratios
E   ModuleNotFoundError: No module named 'ir_simulator'
=============================== warnings summary ===============================
../../../../../opt/homebrew/Caskroom/miniconda/base/lib/python3.13/site-packages/requests/__init__.py:113
  /opt/homebrew/Caskroom/miniconda/base/lib/python3.13/site-packages/requests/__init__.py:113: RequestsDependencyWarning: urllib3 (2.5.0) or chardet (7.4.3)/charset_normalizer (3.4.4) doesn't match a supported version!
    warnings.warn(

<frozen importlib._bootstrap>:488
  <frozen importlib._bootstrap>:488: DeprecationWarning: builtin type SwigPyPacked has no __module__ attribute

<frozen importlib._bootstrap>:488
  <frozen importlib._bootstrap>:488: DeprecationWarning: builtin type SwigPyObject has no __module__ attribute

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ============================
ERROR SG_proj_009/tests/test_ir_simulator.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
======================== 3 warnings, 1 error in 13.02s =========================

<sys>:0: DeprecationWarning: builtin type swigvarlink has no __module__ attribute

```

## 2. Models Detected
- `SG_proj_009/weights/ir_gnn_v1.pt` (7.71 MB)
- `SG_proj_001/models/model_adhesion.pkl` (0.04 MB)
- `SG_proj_001/models/model_tg.pkl` (0.69 MB)
- `SG_proj_001/models/model_viscosity.pkl` (0.36 MB)
- `SG_proj_001/models/feature_names.pkl` (0.00 MB)
- `SG_proj_001/archive/backup_20260626/model_adhesion.pkl` (4.75 MB)
- `SG_proj_001/archive/backup_20260626/model_tg.pkl` (1.19 MB)
- `SG_proj_001/archive/backup_20260626/model_viscosity.pkl` (3.07 MB)
- `SG_proj_001/archive/backup_20260626/feature_names.pkl` (0.01 MB)
