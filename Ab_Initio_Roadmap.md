# Ab Initio — Build-an-LLM-From-Scratch Roadmap

**An independent capability track · from autograd primitives to a model you can talk to**
**Hard mode · Monday 24 August 2026 → Sunday 7 March 2027 (re-baselined 1 Nov 2026; was Thursday 31 December 2026)**

*This document is the canonical reference for Ab Initio. Use it as project instructions. Each milestone is a self-contained build developed in its own conversation, referencing this roadmap for scope, resources, target ship date, and the "done when" bar. This project is deliberately standalone — it has no code or data dependency on any other project.*

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

Original sequencing (Aug 2026 plan; see the re-baseline below for current dates):

- **Deep-derivation milestones (M0, M1, M3)** — the ones that need a fresh brain — are front-loaded into Aug–Sept.
- **Interruption-tolerant milestones (M4 pretraining, M6 nanochat)** — mostly "launch a run and wait" — sit in the Oct–Nov busy stretch, where deep focus is scarce but supervising a training job is not.
- **Capstone comprehension (M6) and the stretch (M7)** land in the calmer December weeks.
- **Pressure valve:** if the window gets eaten, **M7 is the drop-first**; M2 and M5 are the next-most compressible. The core spine M0→M1→M3→M4→M6 is the non-negotiable path.

**Re-baseline · 1 Nov 2026.** Nothing had shipped by 1 Nov (no tags; M0 is still the scaffold stub), so the plan was ~10 weeks behind. Every milestone keeps its original duration and shifts right by exactly 10 weeks; the new end is **Sun 7 Mar 2027**. What the shift breaks: M0–M2 now land in the tail of the busy window instead of calm Aug–Sept, so expect them to run slow; M4 (run-and-wait) now straddles the holidays, which suits it; and the plan now runs into Vertex's Jan–Mar 2027 window, so Vertex's post-training work waits for M5 to ship (see *Hand-off to Vertex*). M3, the centerpiece derivation, now runs Nov 30 – Dec 20, into the pre-Christmas weeks: confirm that focus time is protected, and if it isn't, give M3 one extra week and shift everything after it by 7 days. The pressure valve is unchanged: M7 drops first, then M2/M5 compress.

**Checkpoint:** if M0 hasn't shipped by **Sun Nov 8**, re-baseline again using actual weekly hours, not 10.

| Block | Milestone | Weeks | Dates | Target ship | Est. |
|---|---|---|---|---|---|
| A · Foundations | M0 `ab-grad` | W1 | Nov 2 – Nov 8 | **Sun Nov 8** | ~6–8h |
| A · Foundations | M1 `ab-makemore` | W2–W3 | Nov 9 – Nov 22 | **Sun Nov 22** | ~8–10h |
| A · Foundations | M2 `ab-bpe` | W4 | Nov 23 – Nov 29 | **Sun Nov 29** | ~8–10h |
| B · The transformer | M3 `ab-gpt` | W5–W7 | Nov 30 – Dec 20 | **Sun Dec 20** | ~12–15h |
| C · Scale it up | M4 `ab-pretrain` | W8–W11 | Dec 21 – Jan 17 | **Sun Jan 17** | ~15–20h |
| C · Scale it up | M5 `ab-finetune` | W12–W13 | Jan 18 – Jan 31 | **Sun Jan 31** | ~12–15h |
| D · Capstone | M6 `ab-chat` | W14–W16 | Feb 1 – Feb 21 | **Sun Feb 21** | ~15–25h |
| E · Convergence | M7 own AI | W17–W18 | Feb 22 – Mar 7 | **Sun Mar 7** | open |

**Full ship-complete by Sunday 7 March 2027** (was 31 December 2026). Apply steps are optional, never gate a ship, and sit outside these estimates; Own-AI Engine setup sits outside the weekly budget.

---

## The core resources

Three resources do the heavy lifting; a fourth is the North Star.

1. **Karpathy — Neural Networks: Zero to Hero.** Intuition and the from-primitives builds. [Course landing](https://karpathy.ai/zero-to-hero.html) · [Repo (notebooks + lecture index)](https://github.com/karpathy/nn-zero-to-hero) · [YouTube playlist](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ)
2. **Raschka — *Build a Large Language Model (From Scratch)*.** The structured PyTorch spine for pretraining and finetuning. [Book (Manning)](https://www.manning.com/books/build-a-large-language-model-from-scratch) · [Official code repo](https://github.com/rasbt/LLMs-from-scratch) · [Companion hub](https://sebastianraschka.com/llms-from-scratch/)
3. **Karpathy — nanochat.** The full-pipeline capstone: tokenization → pretraining → finetuning → eval → inference, to a talkable model on a single GPU node. [Repo](https://github.com/karpathy/nanochat)
4. **North Star — Karpathy — microgpt.** A single 200-line, dependency-free Python file containing the *entire* algorithm: dataset, tokenizer, autograd, GPT-2-like net, Adam, training loop, inference loop. Your comprehension benchmark — by M6 you should read every line and know why it's there. [Web](https://karpathy.ai/microgpt.html) · [Write-up](http://karpathy.github.io/2026/02/12/microgpt/)

---

## Own-AI Track (parallel)

Ab Initio gives me understanding from the inside; the Own-AI track gives me a real model I own and use daily. M4–M6 each end with an optional **Apply** step (max ~1–2h) that points what the milestone taught at the real model. An Apply step starts only after the milestone's done-when bar is met and never gates its ship. M7 is where the two tracks converge.

Four layers, all local on my Mac mini (M4 Pro, 64 GB). Nothing leaves the machine.

| Layer | What | Lands in |
|---|---|---|
| **Engine** | Ollama + an open model. Setup only: one afternoon, **outside the 10 hrs/week budget**. Not hard mode; it's infrastructure. 64 GB comfortably holds a ~14–32B model at 4-bit. | Any time before M6 |
| **Memory** | Local embeddings + retrieval over my own corpus (Substack archive, notes). | M7 |
| **Hands** | Tool use / MCP so it can read files and run small agent loops. | M7 |
| **Voice** | LoRA fine-tune on my writing, with MLX on the Mac. Likely on a smaller sibling of the Engine model (~4–8B trains comfortably in 64 GB). | First cut in M5 Apply → M7 |

**Coach contract carries over.** Engine setup is infrastructure, so following the docs is fine. Everything above it (retrieval, the tool loop, the LoRA) is built the Ab Initio way: I write it, Claude coaches.

---

## Milestones

### M0 · `ab-grad` — Autograd from scratch  · target ship **Sun Nov 8**
**Build:** Your own scalar automatic-differentiation engine (a micrograd rebuild) plus a tiny MLP trained on it end to end.
**Why:** The single highest-leverage stage. Once you've hand-derived and coded the backward pass, nothing higher in the stack stays mysterious.
**Resources:** Zero to Hero — "building micrograd" (watch once, then close it and rebuild) · reference: [karpathy/micrograd](https://github.com/karpathy/micrograd)
**Done when:** Your engine trains a 2-layer MLP on a toy dataset, and gradients match PyTorch `autograd` on the same graph within tolerance.

### M1 · `ab-makemore` — Character-level language model  · target ship **Sun Nov 22**
**Build:** A makemore-style model — bigram table → MLP that generates plausible new strings. Then the "backprop ninja" exercise: backprop through the whole MLP manually, no `loss.backward()`.
**Why:** First real contact with the training loop, loss curves, sampling, train/dev/test splits. Manual backprop cements M0 at tensor scale.
**Resources:** Zero to Hero — makemore parts 1–5 · reference: [karpathy/makemore](https://github.com/karpathy/makemore)
**Done when:** Beats the bigram baseline on held-out loss, you can read the train/val curves, and your manual gradients match autograd.

### M2 · `ab-bpe` — Tokenizer from scratch  · target ship **Sun Nov 29**
**Build:** A byte-pair-encoding tokenizer with working `encode()` / `decode()`, trained on a corpus you choose.
**Why:** A large share of LLM weirdness (spelling, arithmetic, non-English) traces straight to tokenization. Building it removes a whole category of future confusion.
**Resources:** Zero to Hero — the tokenizer / BPE lecture · Raschka, tokenization chapter
**Done when:** Round-trip encode→decode is lossless on held-out text, and you can name two model behaviors your tokenizer choices explain.

### M3 · `ab-gpt` — Attention and the transformer block  · target ship **Sun Dec 20**
**Build:** A minGPT-style decoder-only transformer assembled from primitives you write — self-attention, multi-head, positional encoding, the residual / LayerNorm / MLP block — trained on a small corpus.
**Why:** Where the architecture stops being a diagram. You implement attention as matrix ops and see exactly what a head does. **This is the centerpiece derivation — protect the focus time for it.**
**Resources:** Zero to Hero — "Let's build GPT: from scratch, in code, spelled out" · reference: [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT) · Raschka, attention + model-implementation chapters
**Done when:** Trains and generates coherent local structure, and you can trace a single token's path through one full forward pass on paper.

### M4 · `ab-pretrain` — Pretrain a small GPT + load real weights  · target ship **Sun Jan 17**
**Build:** Pretrain your GPT on a general corpus, then load pretrained GPT-2 weights into *your own* architecture and confirm output parity.
**Why:** Loading real weights into code you wrote is where "I understand LLMs" becomes "I've handled the actual thing." Interruption-tolerant: much of it is launch-a-run-and-wait — right fit for the busy weeks.
**Resources:** Raschka — pretraining chapters (read cold, then implement) · [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) · nanoGPT for a scaled reference
**Done when:** Your architecture reproduces GPT-2's outputs on a fixed prompt within numerical tolerance.
**Apply (optional, not ship-gating, ~1–2h):** Stretch goal: load a small modern open model (Qwen3 0.6B or a small Gemma, e.g. Gemma 3 270M) into *your own* transformer code. First derive what GPT-2 lacks: RoPE, RMSNorm, grouped-query attention, SwiGLU (Qwen3 also adds QK-norm). Timeboxed: stop at 2h wherever you are; full logit parity is a bonus, not the bar. Resources: Raschka's bonus chapters (GPT→Llama conversion, Qwen3 and Gemma 3 from scratch) in [ch05 bonus material](https://github.com/rasbt/LLMs-from-scratch/tree/main/ch05).

### M5 · `ab-finetune` — Classifier head + instruction tuning  · target ship **Sun Jan 31**
**Build:** Two forks of your base model — (a) a text classifier with a classification head, (b) an instruction-follower via supervised finetuning.
**Why:** The boundary where a deterministic base model gets shaped toward a task. You see precisely what changes and what doesn't.
**Resources:** Raschka — finetuning chapters (classification + instruction) · [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)
**Done when:** The classifier beats a sensible baseline on held-out data, and the instruction model follows simple instructions the base model ignores.
**Apply (optional, not ship-gating, ~1–2h):** Learn fine-tuning on your own model first (the build above). Then apply the same idea to the open model: a LoRA adapter trained on your Substack archive with MLX ([mlx-lm](https://github.com/ml-explore/mlx-lm)). This is the first cut of the Own-AI **Voice** layer. Resource: Raschka, Appendix E (LoRA).

### M6 · `ab-chat` — Capstone: a model you can talk to  · target ship **Sun Feb 21**
**Build:** Run nanochat end to end — tokenization, pretraining, finetuning, eval, inference — to a small ChatGPT-style model you can converse with. Log an eval (CORE) score.
**Comprehension gate:** Read all 200 lines of `microgpt.py`. If you can explain every line, the track has landed.
**Why:** The full pipeline, owned start to finish, on a real budget (~$100 on a single GPU node; also runs scaled-down on CPU / Apple Silicon). Largely run-and-wait — tolerates a busy tail.
**Resources:** [karpathy/nanochat](https://github.com/karpathy/nanochat) · [microgpt](https://karpathy.ai/microgpt.html)
**Done when:** A chattable checkpoint, a logged eval score, and you can read microgpt cover to cover with no gaps.
**Apply (optional, not ship-gating, ~1–2h):** Put your model (the nanochat checkpoint) and the Ollama model side by side: same prompts, same eval where it fits, and note where each wins. nanochat serves its own checkpoint; the Ollama model is reached through its local API.

### M7 · From scratch to my own AI — convergence  · target ship **Sun Mar 7**
**Build:** Where Ab Initio and the Own-AI track meet. Bring up the remaining Own-AI layers on the Engine: **Memory** (local embeddings + retrieval over your corpus) and **Hands** (tool use / MCP, small agent loops). Fold in the **Voice** adapter from M5, then use what M0–M6 taught to explain the result from the inside. **Drop-first if the calendar tightens.**
**Why:** The from-scratch work stops being an exercise and becomes the reason you can read, adapt, and debug a model you actually use.
**Resources:** the M4–M6 Apply steps · [Ollama](https://ollama.com) · [mlx-lm](https://github.com/ml-explore/mlx-lm) · [Model Context Protocol](https://modelcontextprotocol.io). Two of the old stretch forks still fit as ways to make the claim: systems/inference (KV-cache, quantization; [karpathy/llm.c](https://github.com/karpathy/llm.c)) and internals probing. Reasoning/RL moves to Vertex (below).
**Done when:** Your own AI runs locally with Memory and at least one of Hands/Voice, you use it daily, and you can make one verifiable, non-obvious claim about it (explained by something you built in M0–M6), backed by a figure or benchmark.

### Hand-off to Vertex
Vertex's post-training trilogy (DPO → GRPO) starts **once M5 ships (Sun Jan 31 at the earliest)**, so it begins after Ab Initio has covered fine-tuning. Until then Ab Initio keeps the full ~10 hrs/week. From February, M6 (mostly run-and-wait) and M7 (drop-first) share time with Vertex; if they collide, the Ab Initio core spine comes first and M7 drops. Vertex targets **my own local model** (the Own-AI Engine, plus the Voice adapter once it exists), measured with **my eval harness** (`common/`). Ab Initio supplies the understanding and the harness; Vertex supplies the post-training.

---

## Milestone summary

| # | Project | Target ship | Ships | Anchor resource |
|---|---|---|---|---|
| M0 | `ab-grad` | Sun Nov 8 | Scalar autograd engine + MLP | [micrograd](https://github.com/karpathy/micrograd) |
| M1 | `ab-makemore` | Sun Nov 22 | Char-level LM + manual backprop | [makemore](https://github.com/karpathy/makemore) |
| M2 | `ab-bpe` | Sun Nov 29 | BPE tokenizer (encode/decode) | ZtH tokenizer + Raschka |
| M3 | `ab-gpt` | Sun Dec 20 | Transformer from primitives | [nanoGPT](https://github.com/karpathy/nanoGPT) |
| M4 | `ab-pretrain` | Sun Jan 17 | Pretrained GPT + GPT-2 weight load | [Raschka repo](https://github.com/rasbt/LLMs-from-scratch) |
| M5 | `ab-finetune` | Sun Jan 31 | Classifier + instruction model | Raschka finetuning |
| M6 | `ab-chat` | Sun Feb 21 | Talkable model + eval score | [nanochat](https://github.com/karpathy/nanochat) |
| M7 | own AI | Sun Mar 7 | Convergence: my own AI, used daily | Ollama · mlx-lm · MCP |

---

## Build conventions

- **One monorepo, milestone per folder.** `ab-initio/` with `m0-grad/`, `m1-makemore/`, … and a shared `common/` for reused utilities (data loaders, plotting, eval harness).
- **Reimplement, don't copy.** Reference repos are for unblocking and cross-checking correctness, never for pasting.
- **Verify against a reference.** Where ground truth exists (PyTorch autograd, GPT-2 weights), assert parity in a test rather than eyeballing.
- **A short note per milestone.** 300–500 words on what the stage revealed, committed with the milestone. The repo is public, so write it knowing that. No obligation to publish it anywhere else.
- **Environment:** Python 3.12, PyTorch, a single GPU where a milestone needs it (M4/M6). Everything before M4 runs on a laptop.

---

## What you can do at the end

- Read and modify any open transformer codebase without hand-holding.
- Trace a token from raw bytes through tokenization, the forward pass, sampling, and back — and say where each behavior comes from.
- Train, finetune, and run a small language model end to end, on hardware you own.
- Read microgpt's 200 lines and understand every one — the whole algorithm, no black boxes.
- Run a local AI you own and use daily, and explain it from the inside.

---

## Status tracker

| # | Project | Target ship | Status | Shipped |
|---|---|---|---|---|
| M0 | `ab-grad` | Sun Nov 8 | Not started | |
| M1 | `ab-makemore` | Sun Nov 22 | Not started | |
| M2 | `ab-bpe` | Sun Nov 29 | Not started | |
| M3 | `ab-gpt` | Sun Dec 20 | Not started | |
| M4 | `ab-pretrain` | Sun Jan 17 | Not started | |
| M5 | `ab-finetune` | Sun Jan 31 | Not started | |
| M6 | `ab-chat` | Sun Feb 21 | Not started | |
| M7 | own AI | Sun Mar 7 | Not started | |

**Overall: 0 of 8 milestones started (checked 1 Nov 2026: no tags, M0 stub untouched).**

---

## Decision log

**1 Nov 2026 · Own-AI track added; M7 becomes convergence; dates re-baselined.**
- **Own-AI track added** (Engine / Memory / Hands / Voice). Ab Initio gives understanding from the inside; this gives a real model I own and use daily. Engine setup is infrastructure, so it sits outside the 10 hrs/week budget.
- **Optional Apply steps (~1–2h)** added to M4 (load Qwen3 0.6B / small Gemma into my code), M5 (LoRA on my Substack archive) and M6 (nanochat vs Ollama side by side). They're optional so they can never threaten the core spine: each starts only after done-when and never gates a ship.
- **M7 replaced:** the pick-one-fork stretch becomes "From scratch to my own AI", the convergence point. Still drop-first.
- **Hand-off to Vertex:** Vertex's post-training trilogy (DPO → GRPO) waits for M5 to ship (Jan 31 at the earliest), so Ab Initio keeps the full ~10 hrs/week until then. It targets my own local model, measured with my eval harness.
- **Re-baselined:** nothing had shipped by 1 Nov, so the plan was ~10 weeks behind. All milestones shift right by 10 weeks with their original durations; the new end is Sun 7 Mar 2027. M6–M7 overlap Vertex from February; the pressure valve is unchanged. M3 (Nov 30 – Dec 20) is flagged for one extra week if pre-Christmas focus time isn't protected.
- **Checkpoint:** if M0 hasn't shipped by Sun Nov 8, re-baseline again using actual weekly hours, not 10.
- **Repo hygiene:** the public roadmap names no other research projects apart from Vertex (my learning track that builds on this one); the standalone line now reads "no code or data dependency on any other project". Added `CLAUDE.md` so the coach contract applies in every Claude Code session, not only when a kickoff prompt is pasted.
- The coach contract is unchanged for every build session, including the Apply steps and the Own-AI layers above the Engine.

---

*Ab Initio · roadmap v3 (hard mode, re-baselined 1 Nov 2026) · window Aug 24 2026 – Mar 7 2027, build weeks from Nov 2 at ~10 hrs/week. Parallel Own-AI track (Engine / Memory / Hands / Voice) with optional Apply steps in M4–M6, converging in M7. Core spine M0→M1→M3→M4→M6 non-negotiable; M7 drop-first, M2/M5 next-most compressible. Resources: Karpathy Zero to Hero, Raschka Build a Large Language Model (From Scratch), nanochat; microgpt as the comprehension North Star. Canonical reference for the Ab Initio project.*
