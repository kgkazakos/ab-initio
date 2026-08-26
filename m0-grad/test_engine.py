"""
Ab Initio · M0 · ab-grad — verification harness (the spec).
These tests fail until engine.py is implemented; they assert parity with PyTorch.
Run (from inside m0-grad/):  pip install torch pytest && pytest -q
"""
import torch
from engine import Value


def test_sanity_check():
    x = Value(-4.0)
    z = 2 * x + 2 + x
    q = z.relu() + z * x
    h = (z * z).relu()
    y = h + q + q * x
    y.backward()
    xmg, ymg = x, y

    xt = torch.Tensor([-4.0]).double()
    xt.requires_grad = True
    z = 2 * xt + 2 + xt
    q = z.relu() + z * xt
    h = (z * z).relu()
    y = h + q + q * xt
    y.backward()
    xpt, ypt = xt, y

    assert abs(ymg.data - ypt.data.item()) < 1e-6          # forward pass
    assert abs(xmg.grad - xpt.grad.item()) < 1e-6          # backward pass


def test_more_ops():
    a = Value(-4.0)
    b = Value(2.0)
    c = a + b
    d = a * b + b**3
    c += c + 1
    c += 1 + c + (-a)
    d += d * 2 + (b + a).relu()
    d += 3 * d + (b - a).relu()
    e = c - d
    f = e**2
    g = f / 2.0
    g += 10.0 / f
    g.backward()
    amg, bmg, gmg = a, b, g

    a = torch.Tensor([-4.0]).double(); a.requires_grad = True
    b = torch.Tensor([2.0]).double();  b.requires_grad = True
    c = a + b
    d = a * b + b**3
    c = c + c + 1
    c = c + 1 + c + (-a)
    d = d + d * 2 + (b + a).relu()
    d = d + 3 * d + (b - a).relu()
    e = c - d
    f = e**2
    g = f / 2.0
    g = g + 10.0 / f
    g.backward()
    apt, bpt, gpt = a, b, g

    tol = 1e-6
    assert abs(gmg.data - gpt.data.item()) < tol           # forward pass
    assert abs(amg.grad - apt.grad.item()) < tol           # dg/da
    assert abs(bmg.grad - bpt.grad.item()) < tol           # dg/db
