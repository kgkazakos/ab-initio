"""
Ab Initio · M0 · ab-grad
train_demo.py — train a 2-layer MLP on a toy dataset using YOUR engine.
This is the M0 'done when': a decision boundary on a non-linearly-separable set.
Fill in the TODOs (SVM max-margin loss + small L2, manual SGD with decaying lr).
"""
from nn import MLP


def make_moons(n=100):
    # TODO: generate a 2-class, non-linearly-separable toy set.
    # Hand-roll it, or allow sklearn.datasets.make_moons as a data-only dependency.
    raise NotImplementedError


def loss(model, X, y):
    # TODO: svm max-margin loss + small L2 reg; return (total_loss, accuracy)
    raise NotImplementedError


def train(steps=100):
    model = MLP(2, [16, 16, 1])
    X, y = make_moons()
    for k in range(steps):
        # TODO: forward -> loss -> model.zero_grad() -> loss.backward() -> SGD step
        raise NotImplementedError


if __name__ == "__main__":
    train()
