# M1 · ab-makemore — Character-level LM · ship Sun Sep 13

**Build:** makemore-style model (bigram table -> MLP) that generates plausible strings,
then the "backprop ninja" exercise — backprop the whole MLP manually, no `loss.backward()`.
**Done when:** beats the bigram baseline on held-out loss, you can read the train/val
curves, and your manual gradients match autograd.
Design this milestone in its own conversation (see PROMPTS.md).
