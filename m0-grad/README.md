# M0 · ab-grad — Autograd from scratch · ship Sun Aug 30

**Build:** your own scalar autograd engine (micrograd rebuild) + a 2-layer MLP trained on it.
**Done when:** the engine trains a 2-layer MLP on a toy dataset, and gradients match
PyTorch `autograd` on the same graph within tolerance.

Files: `engine.py` (Value — stubbed), `nn.py` (Neuron/Layer/MLP — stubbed),
`test_engine.py` (spec; fails until engine works), `train_demo.py` (done-when demo).

    pip install torch pytest && pytest -q
