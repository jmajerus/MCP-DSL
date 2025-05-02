# Issues and Challenges in Evolving MCP-DSL

This document collects open questions, architectural tensions, and anticipated edge cases that may impact the design and adoption of MCP-DSL — particularly as it grows from a lightweight orchestrator to a full domain-spanning protocol language.

---

## 🔄 Finite State Machine (FSM) Complexity

**Can MCP-DSL represent a full FSM for interaction workflows?**

* The existing `stateflow` primitive (planned) allows for declarative state transitions, which works well for linear or branching flows.
* But representing complex FSMs with hundreds of states and transitions (e.g., UI navigation, multi-agent coordination, or game engines) may challenge the current flat syntax.

**Possible challenges:**

* Syntax bloat or unreadability
* Tooling complexity for validation and visualization
* Need for nesting or grouping of states

**Possible solutions:**

* Introduce `substate`, `superstate`, or `region` constructs
* Allow FSMs to be imported as modules
* Support external format conversion (e.g. JSON FSM to `.mcpe` DSL)

---

## 📐 Nested/Recursive Binding Paths

**Can we bind deeply nested model outputs or context fields?**

```mcp
bind output.data.person.profile.image.url to Session.lastAvatar
```

* Currently, binding syntax is clean and flat.
* But deeply nested or optional chaining scenarios may require DSL enhancements (e.g. dot-path safety, guards, null coalescing).

---

## 🔧 Schema Validation and Type Safety

* MCP-DSL is designed to be expressive and readable — not necessarily strongly typed.
* Introducing too much schema rigidity might defeat the goal of fluid, prompt-aligned design.
* But **tooling support** (e.g. editors, compilers) benefits from some type predictability.

**Questions:**

* Should `.mcpe` files support optional `type` declarations?
* Can we align with existing standards like JSON Schema, Protobuf, or GraphQL?

---

## 🔁 Infinite or Cyclic Agent Plans

* An `agent` might recurse into itself or spawn cycles unintentionally.
* How can we detect/prevent non-terminating plans or resource exhaustion?

**Possible approaches:**

* Static analysis pass for DAG validation
* Runtime safeguards via TTL (time-to-live) or depth limits

---

## 🛠 Ecosystem Fragmentation Risk

* Introducing `.mcpe` as a superset is pragmatic — but may splinter tooling if not standardized.

**Mitigation:**

* Publish a stable `.mcpe` subset spec
* Provide auto-transpilation to `.mcp-compatible` mode
* Encourage a clear "core" vs. "extended" split

---

## 🤝 Interoperability with Other Agent Frameworks

* Can `.mcpe` interact safely with LangChain, CrewAI, or OpenAI function calling?
* Can we serve `.mcpe` as OpenAPI/JSON for downstream integration?

---

This document will evolve as the language grows. It’s a living register of what we don’t yet know — and a guide for future contributors and implementers.
