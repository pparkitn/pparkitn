# Free GPU Training on Kaggle

A practical guide to maximizing free GPU hours on Kaggle for ML/DL training.

## Free GPU Allowances (as of 2026)

| Resource | Hours/Week | Session Limit | Max Runtime |
|---|---|---|---|
| **Kaggle Notebooks** | 30 hours | 4 concurrent | 9 hours |
| **Kaggle Notebooks (Verified)** | +20 hours bonus | — | — |
| **Kaggle Models** | Unlimited inference | — | — |

## Getting Started

1. **Verify your account**: Phone verification unlocks bonus GPU hours
2. **Enable GPU**: In notebook settings → Accelerator → GPU (Tesla P100 or T4)
3. **Pin your kernel**: Prevents preemption during long training runs

## Optimization Tips

### Maximize Weekly Hours
- **Run 4 sessions concurrently** — Kaggle allows up to 4 parallel GPU sessions
- **Chain 9-hour kernels** — Use checkpointing to resume training across sessions
- **Use "Run on GPU" button** — Avoids CPU-only fallback

### Prevent Session Timeout
The `noscreenlock.ipynb` pattern (in this repo's kaggle collection) keeps the browser tab active:
```javascript
// Inject via browser console or use the notebook
setInterval(() => {
  fetch('/api/heartbeat'); // Keeps session alive
}, 60000);
```

### Data Management
- **Use Kaggle Datasets** — Mount directly: `kaggle datasets download -d user/dataset`
- **Cache weights**: Save checkpoints to `/kaggle/working/` (persists across sessions)
- **Dataset versioning**: `kaggle datasets version -p /path -m "v1.0"`

### Memory & Speed
- **Gradient accumulation**: Simulate larger batch sizes
- **Mixed precision**: `torch.cuda.amp` for 2x speedup on T4/P100
- **Gradient checkpointing**: Trade compute for memory

## Quick Commands

```bash
# Install Kaggle CLI
pip install kaggle

# Authenticate (download kaggle.json from Account page)
mkdir -p ~/.kaggle && cp kaggle.json ~/.kaggle/ && chmod 600 ~/.kaggle/kaggle.json

# Push notebook
kaggle kernels push -p /path/to/notebook

# Create dataset
kaggle datasets init -p /path/to/data
kaggle datasets create -p /path/to/data --public

# Version dataset
kaggle datasets version -p /path/to/data -m "v1.1: added validation split"
```

## Resources in This Repo
- `kaggle_dataset/README.md` — Detailed dataset creation guide
- `extra/papermill.md` — Automated notebook scheduling
- `extra/spark.md` — PySpark on Kaggle (CPU only, for data prep)

## Pro Tips
- **Friday evening starts** — Fresh weekly quota resets weekly (usually Monday UTC)
- **Avoid peak hours** — GPU contention lower early mornings/late nights
- **Pre-download weights** — Use `kaggle datasets download` in init cell to cache locally
- **Monitor usage**: Profile → GPU Usage dashboard