# Step 4 — prepare the local training tools

**Learn:** a separate Python environment keeps training dependencies separate from
the app. Recording exact package versions helps reproduce an experiment.

PyTorch performs the numerical calculations and computes gradients: how the loss
changes when a model weight changes. An optimiser later uses those gradients to
update weights. Installing PyTorch does not install a trained model.

## Reproduce the setup

Run from the repository root on this Apple Silicon Mac, using the installed `uv`
package manager and Python 3.14.3. The requirements file records the packages
resolved on macOS; other platforms need their own compatibility check.

```sh
uv venv runs/lesson01-env --python .venv/bin/python --no-project --cache-dir runs/uv-cache
uv pip install --python runs/lesson01-env/bin/python --cache-dir runs/uv-cache --only-binary :all: -r requirements-training-macos.txt
```

Use these setup commands for a fresh environment. For an existing environment,
check its packages before replacing or reinstalling anything. `runs/` is ignored
by Git. The installed environment stays local; its requirements and these
instructions are saved in the repository. The app's `.venv` is unchanged.

PyTorch's [package metadata](https://pypi.org/project/torch/) and
[licence notices](https://github.com/pytorch/pytorch/blob/main/LICENSE) describe
its permissive licences, including third-party components. The installation
downloads software libraries, not pretrained weights or external training data.
The exercise uses our fictional examples and will start from random weights.

## Check the calculation and local save/reload

This checks a scalar calculation on the CPU, not a trained poster generator:

```sh
runs/lesson01-env/bin/python - <<'PY'
from pathlib import Path
import torch

w = torch.tensor(2.0, requires_grad=True)
loss = (3 * w) ** 2
loss.backward()
assert loss.item() == 36.0
assert w.grad.item() == 36.0
assert w.item() == 2.0  # Calculating a gradient does not update the weight.
path = Path("runs/lesson01-preflight.pt")
torch.save({"w": w.detach()}, path)
print("PASS: CPU calculation, gradient and save; no weight update")
PY

runs/lesson01-env/bin/python - <<'PY'
import torch
saved = torch.load("runs/lesson01-preflight.pt", map_location="cpu", weights_only=True)
assert saved["w"].item() == 2.0
print("PASS: saved scalar reloaded in a fresh process")
PY
```

The first calculation has an answer known in advance: the loss and its gradient
are both 36 at `w = 2`. A passing check establishes that these basic operations
work. It does not establish sequence-model training, memory fit for that model,
accelerator support, or model checkpoint recovery.

**Next:** inspect a real brief/layout batch, including the next-token shift and
which labels count toward loss. Then construct and run the bounded training loop.
