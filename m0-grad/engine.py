"""
Ab Initio · M0 · ab-grad
engine.py — a scalar reverse-mode autograd engine (your micrograd rebuild).

Fill in the TODOs. Do NOT copy from karpathy/micrograd — watch the lecture once,
then write this yourself. test_engine.py is the spec: it checks both the forward
values and that .grad matches PyTorch autograd on the same graph.

Contract:
  - Value(data) wraps a float and accumulates a gradient in .grad.
  - Each op returns a new Value and wires a local _backward() closure that
    propagates out.grad into the inputs' .grad via the chain rule.
  - backward() runs a reverse-topological pass from this node: seed self.grad=1.0,
    then call each node's _backward() in reverse order.
"""


class Value:
    def __init__(self, data, _children=(), _op=""):
        self.data = float(data)
        self.grad = 0.0
        self._backward = lambda: None      # each op overwrites this
        self._prev = set(_children)
        self._op = _op

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data, (self, other), "+")

        def _backward():
            # TODO: d(out)/d(self) = 1 ; d(out)/d(other) = 1  (remember: accumulate)
            raise NotImplementedError
        out._backward = _backward
        return out

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, (self, other), "*")

        def _backward():
            # TODO: product rule
            raise NotImplementedError
        out._backward = _backward
        return out

    def __pow__(self, other):
        assert isinstance(other, (int, float)), "only int/float powers supported"
        out = Value(self.data ** other, (self,), f"**{other}")

        def _backward():
            # TODO: power rule
            raise NotImplementedError
        out._backward = _backward
        return out

    def relu(self):
        out = Value(0.0 if self.data < 0 else self.data, (self,), "ReLU")

        def _backward():
            # TODO
            raise NotImplementedError
        out._backward = _backward
        return out

    def tanh(self):
        # Optional, but convenient for the MLP. Implement if you use it.
        raise NotImplementedError

    def exp(self):
        raise NotImplementedError

    def backward(self):
        # TODO:
        #   1. build a reverse-topological ordering of the graph reachable from self
        #   2. seed self.grad = 1.0
        #   3. for node in reversed(topo): node._backward()
        raise NotImplementedError

    # --- convenience wrappers (work once the core ops above are done) ---
    def __neg__(self): return self * -1
    def __radd__(self, other): return self + other
    def __sub__(self, other): return self + (-other)
    def __rsub__(self, other): return other + (-self)
    def __rmul__(self, other): return self * other
    def __truediv__(self, other): return self * other ** -1
    def __rtruediv__(self, other): return other * self ** -1
    def __repr__(self): return f"Value(data={self.data}, grad={self.grad})"
