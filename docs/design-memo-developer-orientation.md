# Developer Orientation: Design Philosophy of MCP-DSL

This memo outlines key architectural choices and guiding principles behind the MCP-DSL project. It is intended for contributors, tool integrators, and curious developers wondering: *Why does this system work the way it does?* And how do we keep it from becoming another overengineered framework?

---

## 🧠 Separation of Concerns: Protocol vs. Configuration

We separate `.mcpe` (behavioral orchestration) from `.mcp` (model and system configuration). While this introduces complexity, it brings long-term clarity:

* **`.mcpe`** files describe *how models interact with context* in workflows
* **`.mcp`** files describe *what a model is and how it’s configured*

This lets us:

* Reuse model configs across multiple workflows
* Evolve orchestration logic without redefining model specs
* Keep orchestration readable and composable

This separation is modeled after real-world practice in AI/ML, not imagined ideals.

---

## 🔍 Acknowledging Real-World Tension

We recognize that developers often need a *unified view*. Having protocol and config split across files introduces friction unless:

* There are cross-links (`@config:` in `.mcpe` and `bound_protocol:` in `.mcp`)
* There’s tooling to visualize them together
* Assistants or preprocessors help bridge the view

So we design for *both clarity and composability*, while anticipating future tools.

---

## ✅ Why This Isn’t “Another Globus”

MCP-DSL is intentionally:

* Lightweight
* Declarative, not imperative
* Text-based, not reliant on any single backend or runtime
* GPT-assistable but not GPT-dependent

We aim for the power of `Dockerfile`, `Makefile`, or `GraphQL`, not a monolithic orchestrator.

---

## 🧠 Prompt + Protocol = Partnership

While GPTs can generate `.mcp` or `.mcpe` files, they can’t (yet):

* Validate consistency across config and logic
* Visualize fallback flows or concurrency semantics
* Generate repeatable, self-documenting pipelines by default

MCP-DSL gives structure to what GPTs *describe* — and a durable artifact to what would otherwise be an ephemeral chat.

---

## 🌉 A Platform for Tools, Not a Tool Itself

This project isn’t just a DSL — it’s a foundation:

* For agent workflows
* For domain-specific model coordination
* For visual editors, code generators, doc generators, and static analyzers

We’re building the language **we wish AI workflows had from the beginning.**

---

## 🎯 TL;DR

MCP-DSL is:

* Structured enough for static analysis
* Composable enough for teams
* Clear enough for GPT collaboration
* Declarative enough to avoid entanglement
* Open enough to support multi-domain extensions

We don’t intend to replace prompts.
We intend to catch them, organize them, and give them somewhere reliable to land.
