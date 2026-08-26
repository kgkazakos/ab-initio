# Ab Initio — Build-an-LLM-From-Scratch Roadmap

**An independent capability track · from autograd primitives to a model you can talk to**
**Hard mode · Monday 24 August 2026 → Thursday 31 December 2026 (~18.5 weeks)**

*This document is the canonical reference for Ab Initio. Use it as project instructions. Each milestone is a self-contained build developed in its own conversation, referencing this roadmap for scope, resources, target ship date, and the "done when" bar. This project is deliberately standalone — it shares no content, vocabulary, or dependency with any other project.*

*Name is a placeholder (alt: Anvil). "Ab initio" = from first principles, no fitted shortcuts — the project's ethic: build the model up from primitives rather than call a pretrained API.*

---

## How to use this document

- **One conversation per milestone.** Start a new chat for each milestone (M0–M7), pasting the relevant section as scope.
- **Build-first, not watch-first.** Every milestone ships a working artifact you wrote. Watch/read to unblock, never to complete.
- **Reimplement, don't copy.** Type every line. If you paste from a reference repo, you didn't learn it. The point is the mechanical fluency — autograd, the backward pass, the training loop — that reading can't give you.
- **Status tracking is at the end** — update as milestones ship.

---

## Timeline & cadence — hard mode

**Target load: ~10 focused hours/week** (up from the sustainable 4–6). Core path M0–M6 is ~95 hours of work; at this pace the calendar, not the hours, is the binding constraint.

The schedule is **sequenced against a heavy quarter**, not just compressed. This runs concurrent with a parallel build track and a known-busy Sept–Nov window (new arrival + a race). So the ordering is deliberate:

- **Deep-derivation milestones (M0, M1, M3)** — the ones that need a fresh brain — are front-loaded into Aug–Sept.
- **Interruption-tolerant milestones (M4 pretraining, M6 nanochat)** — mostly "launch a run and wait" — sit in the Oct–Nov busy stretch, where deep focus is scarce but supervising a training job is not.
- **Capstone comprehension (M6) and the stretch (M7)** land in the calmer December weeks.
- **Pressure valve:** if the window gets eaten, **M7 is the drop-first**; M2 and M5 are the next-most compressible. The core spine M0→M1→M3→M4→M6 is the non-negotiable path.

| Block | Milestone | Weeks | Dates | Target ship | Est. |
|---|---|---|---|---|---|
| A · Foundations | M0 `ab-grad` | W1 | Aug 24 – Aug 30 | **Sun Aug 30** | ~6–8h |
| A · Foundations | M1 `ab-makemore` | W2–W3 | Aug 31 – Sep 13 | **Sun Sep 13** | ~8–10h |
| A · Foundations | M2 `ab-bpe` | W4 | Sep 14 – Sep 20 | **Sun Sep 20** | ~8–10h |
| B · The transformer | M3 `ab-gpt` | W5–W7 | Sep 21 – Oct 11 | **Sun Oct 11** | ~12–15h |
| C · Scale it up | M4 `ab-pretrain` | W8–W11 | Oct 12 – Nov 8 | **Sun Nov 8** | ~15–20h |
| C · Scale it up | M5 `ab-finetune` | W12–W13 | Nov 9 – Nov 22 | **Sun Nov 22** | ~12–15h |
| D · Capstone | M6 `ab-chat` | W14–W16 | Nov 23 – Dec 13 | **Sun Dec 13** | ~15–25h |
| E · Stretch | M7 stretch | W17–W19 | Dec 14 – Dec 31 | **Wed Dec 31** | open |

**Full ship-complete by 31 December 2026.**

---

## The core resources

Three resources do the heavy lifting; a fourth is the North Star.

1. **Karpathy — Neural Networks: Zero to Hero.** Intuition and the from-primitives builds. [Course landing](https://karpathy.ai/zero-to-hero.html) · [Repo (notebooks + lecture index)](https://github.com/karpathy/nn-zero-to-hero) · [YouTube playlist](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ)
2. **Raschka — *Build a Large Language Model (From Scratch)*.** The structured PyTorch spine for pretraining and finetuning. [Book (Manning)](https://www.manning.com/books/build-a-large-language-model-from-scratch) · [Official code repo](https://github.com/rasbt/LLMs-from-scratch) · [Companion hub](https://sebastianraschka.com/llms-from-scratch/)
3. **Karpathy — nanochat.** The full-pipeline capstone: tokenization → pretraining → finetuning → eval → inference, to a talkable model on a single GPU node. [Repo](https://github.com/karpathy/nanochat)
4. **North Star — Karpathy — microgpt.** A single 200-line, dependency-free Python file containing the *entire* algorithm: dataset, tokenizer, autograd, GPT-2-like net, Adam, training loop, inference loop. Your comprehension benchmark — by M6 you should read every line and know why it's there. [Web](https://karpathy.ai/microgpt.html) · [Write-up](http://karpathy.github.io/2026/02/12/microgpt/)

---

## Milestones

### M0 · `ab-grad` — Autograd from scratch  · target ship **Sun Aug 30**
**Build:** Your own scalar automatic-differentiation engine (a micrograd rebuild) plus a tiny MLP trained on it end to end.
**Why:** The single highest-leverage stage. Once you've hand-derived and coded the backward pass, nothing higher in the stack stays mysterious.
**Resources:** Zero to Hero — "building micrograd" (watch once, then close it and rebuild) · reference: [karpathy/micrograd](https://github.com/karpathy/micrograd)
**Done when:** Your engine trains a 2-layer MLP on a toy dataset, and gradients match PyTorch `autograd` on the same graph within tolerance.

### M1 · `ab-makemore` — Character-level language model  · target ship **Sun Sep 13**
**Build:** A makemore-style model — bigram table → MLP that generates plausible new strings. Then the "backprop ninja" exercise: backprop through the whole MLP manually, no `loss.backward()`.
**Why:** First real contact with the training loop, loss curves, sampling, train/dev/test splits. Manual backprop cements M0 at tensor scale.
**Resources:** Zero to Hero — makemore parts 1–5 · reference: [karpathy/makemore](https://github.com/karpathy/makemore)
**Done when:** Beats the bigram baseline on held-out loss, you can read the train/val curves, and your manual gradients match autograd.

### M2 · `ab-bpe` — Tokenizer from scratch  · target ship **Sun Sep 20**
**Build:** A byte-pair-encoding tokenizer with working `encode()` / `decode()`, trained on a corpus you choose.
**Why:** A large share of LLM weirdness (spelling, arithmetic, non-English) traces straight to tokenization. Building it removes a whole category of future confusion.
**Resources:** Zero to Hero — the tokenizer / BPE lecture · Raschka, tokenization chapter
**Done when:** Round-trip encode→decode is lossless on held-out text, and you can name two model behaviors your tokenizer choices explain.

### M3 · `ab-gpt` — Attention and the transformer block  · target ship **Sun Oct 11**
**Build:** A minGPT-style decoder-only transformer assembled from primitives you write — self-attention, multi-head, positional encoding, the residual / LayerNorm / MLP block — trained on a small corpus.
**Why:** Where the architecture stops being a diagram. You implement attention as matrix ops and see exactly what a head does. **This is the centerpiece derivation — protect the focus time for it.**
**Resources:** Zero to Hero — "Let's build GPT: from scratch, in code, spelled out" · reference: [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT) · Raschka, attention + model-implementation chapters
**Done when:** Trains and generates coherent local structure, and you can trace a single token's path through one full forward pass on paper.

### M4 · `ab-pretrain` — Pretrain a small GPT + load real weights  · target ship **Sun Nov 8**
**Build:** Pretrain your GPT on a general corpus, then load pretrained GPT-2 weights into *your own* architecture and confirm output parity.
**Why:** Loading real weights into code you wrote is where "I understand LLMs" becomes "I've handled the actual thing." Interruption-tolerant: much of it is launch-a-run-and-wait — right fit for the busy weeks.
**Resources:** Raschka — pretraining chapters (read cold, then implement) · [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) · nanoGPT for a scaled reference
**Done when:** Your architecture reproduces GPT-2's outputs on a fixed prompt within numerical tolerance.

### M5 · `ab-finetune` — Classifier head + instruction tuning  · target ship **Sun Nov 22**
**Build:** Two forks of your base model — (a) a text classifier with a classification head, (b) an instruction-follower via supervised finetuning.
**Why:** The boundary where a deterministic base model gets shaped toward a task. You see precisely what changes and what doesn't.
**Resources:** Raschka — finetuning chapters (classification + instruction) · [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)
**Done when:** The classifier beats a sensible baseline on held-out data, and the instruction model follows simple instructions the base model ignores.

### M6 · `ab-chat` — Capstone: a model you can talk to  · target ship **Sun Dec 13**
**Build:** Run nanochat end to end — tokenization, pretraining, finetuning, eval, inference — to a small ChatGPT-style model you can converse with. Log an eval (CORE) score.
**Comprehension gate:** Read all 200 lines of `microgpt.py`. If you can explain every line, the track has landed.
**Why:** The full pipeline, owned start to finish, on a real budget (~$100 on a single GPU node; also runs scaled-down on CPU / Apple Silicon). Largely run-and-wait — tolerates a busy tail.
**Resources:** [karpathy/nanochat](https://github.com/karpathy/nanochat) · [microgpt](https://karpathy.ai/microgpt.html)
**Done when:** A chattable checkpoint, a logged eval score, and you can read microgpt cover to cover with no gaps.

### M7 · Stretch — pick one fork  · target ship **Wed Dec 31**
Choose the direction you want depth in; scope it in its own conversation. **Drop-first if the calendar tightens.**
- **Reasoning / RL.** Build a reasoning model from scratch — RL post-training, verifiers, chain-of-thought. Anchor: [rasbt/reasoning-from-scratch](https://github.com/rasbt/reasoning-from-scratch).
- **Systems / inference.** KV-cache, quantization, speculative decoding; or go bare-metal with [karpathy/llm.c](https://github.com/karpathy/llm.c) (training in raw C/CUDA).
- **Internals probing.** Attention-pattern visualization and activation probing on your M6 model — understand what your own weights represent.
**Done when:** One verifiable, non-obvious claim about your model or pipeline, backed by a figure or benchmark.

---

## Milestone summary

| # | Project | Target ship | Ships | Anchor resource |
|---|---|---|---|---|
| M0 | `ab-grad` | Sun Aug 30 | Scalar autograd engine + MLP | [micrograd](https://github.com/karpathy/micrograd) |
| M1 | `ab-makemore` | Sun Sep 13 | Char-level LM + manual backprop | [makemore](https://github.com/karpathy/makemore) |
| M2 | `ab-bpe` | Sun Sep 20 | BPE tokenizer (encode/decode) | ZtH tokenizer + Raschka |
| M3 | `ab-gpt` | Sun Oct 11 | Transformer from primitives | [nanoGPT](https://github.com/karpathy/nanoGPT) |
| M4 | `ab-pretrain` | Sun Nov 8 | Pretrained GPT + GPT-2 weight load | [Raschka repo](https://github.com/rasbt/LLMs-from-scratch) |
| M5 | `ab-finetune` | Sun Nov 22 | Classifier + instruction model | Raschka finetuning |
| M6 | `ab-chat` | Sun Dec 13 | Talkable model + eval score | [nanochat](https://github.com/karpathy/nanochat) |
| M7 | stretch | Wed Dec 31 | One deep dive | reasoning-from-scratch / llm.c |

---

## Build conventions

- **One monorepo, milestone per folder.** `ab-initio/` with `m0-grad/`, `m1-makemore/`, … and a shared `common/` for reused utilities (data loaders, plotting, eval harness).
- **Reimplement, don't copy.** Reference repos are for unblocking and cross-checking correctness, never for pasting.
- **Verify against a reference.** Where ground truth exists (PyTorch autograd, GPT-2 weights), assert parity in a test rather than eyeballing.
- **A short note per milestone.** 300–500 words on what the stage revealed. Kept for yourself; no obligation to publish.
- **Environment:** Python 3.12, PyTorch, a single GPU where a milestone needs it (M4/M6). Everything before M4 runs on a laptop.

---

## What you can do at the end

- Read and modify any open transformer codebase without hand-holding.
- Trace a token from raw bytes through tokenization, the forward pass, sampling, and back — and say where each behavior comes from.
- Train, finetune, and run a small language model end to end, on hardware you own.
- Read microgpt's 200 lines and understand every one — the whole algorithm, no black boxes.

---

## Status tracker

| # | Project | Target ship | Status | Shipped |
|---|---|---|---|---|
| M0 | `ab-grad` | Sun Aug 30 | Not started | |
| M1 | `ab-makemore` | Sun Sep 13 | Not started | |
| M2 | `ab-bpe` | Sun Sep 20 | Not started | |
| M3 | `ab-gpt` | Sun Oct 11 | Not started | |
| M4 | `ab-pretrain` | Sun Nov 8 | Not started | |
| M5 | `ab-finetune` | Sun Nov 22 | Not started | |
| M6 | `ab-chat` | Sun Dec 13 | Not started | |
| M7 | stretch | Wed Dec 31 | Not started | |

**Overall: 0 of 8 milestones started.**

---

*Ab Initio · roadmap v2 (hard mode) · window Aug 24 – Dec 31 2026, ~18.5 weeks at ~10 hrs/week. Sequenced against a heavy quarter: deep-derivation milestones (M0/M1/M3) front-loaded, interruption-tolerant milestones (M4/M6) placed in the busy stretch, capstone + stretch in December. Core spine M0→M1→M3→M4→M6 non-negotiable; M7 drop-first, M2/M5 next-most compressible. Resources: Karpathy Zero to Hero, Raschka Build a Large Language Model (From Scratch), nanochat; microgpt as the comprehension North Star. Canonical reference for the Ab Initio project.*
