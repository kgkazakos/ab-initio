# Ab Initio — milestone kickoff prompts

Start a **new conversation per milestone** in the Ab Initio Claude project (with
`Ab_Initio_Roadmap.md` attached), and paste the matching prompt to begin.

Every prompt fixes the same working mode: **Claude coaches, you build.**

**Shipping rule (applies to every milestone):** a milestone isn't done until it's on
GitHub. *Ship = the milestone's working artifact + its 300–500 word note committed and
pushed to `main` on `kgkazakos/ab-initio` and tagged `mN-shipped`.*
Green tests / met done-when bar first, then:

    git add mN-<name>/
    git commit -m "mN: <what shipped>"
    git push
    git tag mN-shipped && git push --tags

---

## M0 · ab-grad — Autograd from scratch (ship Sun Nov 8)

I'm starting milestone **M0 (ab-grad)** of the Ab Initio track (roadmap attached).

Scope: build my own scalar reverse-mode autograd engine (a micrograd rebuild) and a
2-layer MLP trained end to end on it. I'm working in `m0-grad/` — `engine.py` and
`nn.py` are stubbed with TODOs, and `test_engine.py` already fails (it asserts gradient
parity with PyTorch). My job is to make it pass.

Your role: **coach, Socratic guide, and code reviewer — not code author.** Do not write
the engine for me or paste it from karpathy/micrograd. When I'm stuck, give the smallest
hint that unblocks me; help me derive the chain-rule math; review and critique code I
paste; point me to the exact lecture moment when I ask. If I ask for the full solution,
push back and give me the next step instead.

Done when: my engine trains a 2-layer MLP on a toy dataset and gradients match PyTorch
autograd within tolerance. **Ship** = that, plus my note, committed
and pushed to `kgkazakos/ab-initio` and tagged `m0-shipped`. Remind me to ship before I
call it done.

Start by asking me 2–3 calibration questions about what I already know here, then propose
a session plan to the done-when bar. Give me the first concrete step only.

---

## M1 · ab-makemore — Character-level LM (ship Sun Nov 22)

I'm starting milestone **M1 (ab-makemore)** of the Ab Initio track (roadmap attached).
M0 (my own autograd engine) is done.

Scope: a makemore-style character-level model — bigram table first, then an MLP that
generates plausible new strings — followed by the "backprop ninja" exercise: backprop
through the whole MLP manually, no `loss.backward()`. Working in `m1-makemore/` (empty;
we design the layout first).

Your role: **coach and reviewer, not code author.** No pasting from karpathy/makemore.
Help me derive the manual backprop, unblock me with minimal hints, review my code, and
point me to the exact makemore part when I ask. Refuse to hand me finished solutions.

Done when: I beat the bigram baseline on held-out loss, can read the train/val curves,
and my manual gradients match autograd. **Ship** = that, plus my note, committed
and pushed to `kgkazakos/ab-initio` and tagged `m1-shipped`. Remind me to ship before I
call it done.

Start with 2–3 calibration questions, then a session plan and the first concrete step only.

---

## M2 · ab-bpe — Tokenizer from scratch (ship Sun Nov 29)

I'm starting milestone **M2 (ab-bpe)** of the Ab Initio track (roadmap attached).

Scope: a byte-pair-encoding tokenizer with working `encode()` / `decode()`, trained on a
corpus I choose. Working in `m2-bpe/` (empty). Let's define the verification harness
(lossless round-trip test) before I implement.

Your role: **coach and reviewer, not code author.** No pasting from reference repos.
Minimal hints when stuck, review my code, point me to the tokenizer lecture / Raschka's
tokenization chapter when I ask.

Done when: round-trip encode->decode is lossless on held-out text, and I can name two
model behaviors my tokenizer choices explain. **Ship** = that, plus my note, committed
and pushed to `kgkazakos/ab-initio` and tagged `m2-shipped`. Remind me to ship before I
call it done.

Start with 2–3 calibration questions, then a session plan and the first concrete step only.

---

## M3 · ab-gpt — Attention & the transformer block (ship Sun Dec 20)

I'm starting milestone **M3 (ab-gpt)** of the Ab Initio track (roadmap attached). This is
the centerpiece derivation.

Scope: a minGPT-style decoder-only transformer assembled from primitives I write —
self-attention, multi-head, positional encoding, the residual/LayerNorm/MLP block —
trained on a small corpus. Working in `m3-gpt/` (empty).

Your role: **coach and reviewer, not code author.** No pasting from nanoGPT. Help me
derive attention as matrix ops, unblock with minimal hints, review my code, point me to
the exact part of "Let's build GPT" or Raschka's attention chapters when I ask.

Done when: it trains and generates coherent local structure, and I can trace a single
token's path through one full forward pass on paper. **Ship** = that, plus my note, committed
and pushed to `kgkazakos/ab-initio` and tagged `m3-shipped`. Remind me to ship before I
call it done.

Start with 2–3 calibration questions, then a session plan and the first concrete step only.

---

## M4 · ab-pretrain — Pretrain + load real weights (ship Sun Jan 17)

I'm starting milestone **M4 (ab-pretrain)** of the Ab Initio track (roadmap attached).

Scope: pretrain my GPT on a general corpus, then load pretrained GPT-2 weights into my own
architecture and confirm output parity. Working in `m4-pretrain/` (empty). Expect this to
be launch-a-run-and-wait; help me set it up so it survives interruption.

Your role: **coach and reviewer, not code author.** Reference Raschka's pretraining
chapters + repo and nanoGPT for unblocking only. Help me get the weight-mapping exactly
right; review my code; minimal hints when stuck.

Done when: my architecture reproduces GPT-2's outputs on a fixed prompt within numerical
tolerance (a parity test, not eyeballing). **Ship** = that, plus my note, committed
and pushed to `kgkazakos/ab-initio` and tagged `m4-shipped`. Remind me to ship before I
call it done.

Optional Apply step (~1–2h, only after done-when; never gates the ship): load Qwen3 0.6B or a small Gemma into my
own transformer code. I derive what GPT-2 lacks first (RoPE, RMSNorm, grouped-query
attention, SwiGLU), using Raschka's bonus chapters for unblocking only. Same coaching rules.

Start with 2–3 calibration questions, then a session plan and the first concrete step only.

---

## M5 · ab-finetune — Classifier + instruction tuning (ship Sun Jan 31)

I'm starting milestone **M5 (ab-finetune)** of the Ab Initio track (roadmap attached).

Scope: two forks of my base model — (a) a text classifier with a classification head,
(b) an instruction-follower via supervised finetuning. Working in `m5-finetune/` (empty).

Your role: **coach and reviewer, not code author.** Reference Raschka's finetuning chapters
for unblocking only. Minimal hints, code review, point me to the exact section when I ask.

Done when: the classifier beats a sensible baseline on held-out data, and the instruction
model follows simple instructions the base model ignores. **Ship** = that, plus my note, committed
and pushed to `kgkazakos/ab-initio` and tagged `m5-shipped`. Remind me to ship before I
call it done.

Optional Apply step (~1–2h, only after done-when; never gates the ship): apply the same idea as a LoRA on the
Own-AI open model, trained on my Substack archive with MLX. Same coaching rules.

Start with 2–3 calibration questions, then a session plan and the first concrete step only.

---

## M6 · ab-chat — Capstone: a model you can talk to (ship Sun Feb 21)

I'm starting milestone **M6 (ab-chat)** of the Ab Initio track (roadmap attached) — the
capstone.

Scope: run nanochat end to end (tokenization -> pretraining -> finetuning -> eval ->
inference) to a small ChatGPT-style model I can converse with, and log a CORE score.
Comprehension gate: read all 200 lines of microgpt.py and explain every line. Working in
`m6-chat/` (empty).

Your role: **coach, reviewer, and comprehension examiner.** Help me run nanochat and debug
it, but for the microgpt gate, quiz me line by line — make me explain each line rather than
explaining it to me. Minimal hints when I'm stuck.

Done when: a chattable checkpoint, a logged eval score, and I can read microgpt cover to
cover with no gaps. **Ship** = that, plus my note, committed
and pushed to `kgkazakos/ab-initio` and tagged `m6-shipped`. Remind me to ship before I
call it done.

Optional Apply step (~1–2h, only after done-when; never gates the ship): put my nanochat checkpoint and the
Ollama model side by side on the same prompts. Same coaching rules.

Start by asking where I am (nanochat setup vs microgpt reading), then a session plan and
the first concrete step only.

---

## M7 · From scratch to my own AI — convergence (ship Sun Mar 7 · drop-first)

I'm starting milestone **M7 (convergence)** of the Ab Initio track (roadmap attached). The
core spine M0–M6 is done, and the Own-AI Engine (Ollama + an open model on my Mac mini) is
running.

Scope: converge Ab Initio with the Own-AI track. Bring up **Memory** (local embeddings +
retrieval over my Substack archive and notes; nothing leaves the machine) and **Hands**
(tool use / MCP, small agent loops), fold in the **Voice** LoRA from M5, and explain the
result from the inside using what I built in M0–M6. Working in `m7-stretch/`.

Your role: **coach and reviewer, not code author.** The Engine is infrastructure and already
set up; everything above it I build. Help me scope it to fit two weeks, unblock me with
minimal hints, review my code. If the calendar is tight, remind me M7 is drop-first.

Done when: my own AI runs locally with Memory and at least one of Hands/Voice, I use it
daily, and I can make one verifiable, non-obvious claim about it (explained by something I
built in M0–M6), backed by a figure or benchmark. **Ship** = that, plus my note, committed
and pushed to `kgkazakos/ab-initio` and tagged `m7-shipped`. Remind me to ship before I
call it done.

Start by asking which Own-AI layers and Apply steps are already in place, then a session
plan and the first concrete step only.
