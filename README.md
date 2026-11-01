# Ab Initio

Build an LLM from scratch, from autograd primitives to a model you can talk to.
Independent capability track. Hard mode: **Mon 24 Aug 2026 → Sun 7 Mar 2027**
(re-baselined 1 Nov 2026).

The canonical plan is `Ab_Initio_Roadmap.md`. Kickoff prompts for each milestone
are in `PROMPTS.md` — start a fresh conversation per milestone and paste the
matching prompt.

A parallel **Own-AI track** (Ollama + an open model, local retrieval, tool use, a
LoRA on my writing) runs alongside and converges with Ab Initio in M7. See the roadmap.

## Structure
    ab-initio/
      Ab_Initio_Roadmap.md   canonical roadmap (scope, ship dates, done-when)
      PROMPTS.md             one kickoff prompt per milestone (M0–M7)
      CLAUDE.md              coach contract, loaded by every Claude Code session
      common/                shared utils, added only when a 2nd milestone needs them
      m0-grad/               autograd engine + MLP        (ship Sun Nov 8)
      m1-makemore/           char-level LM + manual backprop (ship Sun Nov 22)
      m2-bpe/                BPE tokenizer                (ship Sun Nov 29)
      m3-gpt/                transformer from primitives  (ship Sun Dec 20)
      m4-pretrain/           pretrain + load GPT-2 weights (ship Sun Jan 17)
      m5-finetune/           classifier + instruction tune (ship Sun Jan 31)
      m6-chat/               nanochat capstone            (ship Sun Feb 21)
      m7-stretch/            convergence: my own AI       (ship Sun Mar 7)

## Rules
- Reimplement, don't copy. Type every line; reference repos are for unblocking only.
- Every milestone ships a working artifact and a 300–500 word note on what it revealed.
- Verify against a reference (PyTorch autograd, GPT-2 weights) with a test, not by eye.

## Setup
    python3.12 -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt

## M0 quickstart
    cd m0-grad
    pytest -q          # tests fail until you implement engine.py — that's the point
