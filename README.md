# MCP-DSL: A Declarative Language for Model-Context Interaction

⚠️ **DRAFT IN PROGRESS**
This project is under active development. Syntax, structure, and features are subject to change as the MCP specification evolves and this DSL matures.

---

## 🌟 Vision

MCP-DSL is a domain-specific language (DSL) for expressing high-level model and context interaction logic in AI systems. It abstracts away low-level plumbing, enabling developers to describe intent clearly while generating reliable and maintainable backend code.

Whenever high-level orchestration logic is mixed with low-level implementation code, we lose clarity and composability. MCP-DSL separates these layers by giving AI developers a clean language to define:

* **Models** and their input/output types
* **Context containers** and their evolving state
* **Interactions** that connect models to context
* **Protocol rules** for state transitions and binding logic

---

## 💡 Why MCP-DSL?

* ✅ Declarative: Focus on *what* the model should do, not *how* to wire it
* ✅ Safe: Generate validated, structured, auditable code
* ✅ Composable: Reuse and combine model-context patterns
* ✅ Scalable: Add new models or interactions without breaking structure

---

## 🧱 MCP Concepts (Updated)

MCP-DSL builds upon the principles of the [Model Context Protocol (MCP)](https://github.com/anthropics/mcp), extending them into a fully declarative domain-specific language.

> 🛑 **Note:** Early drafts of this project were based on a narrow interpretation of MCP (limited to `model`, `context`, and `interaction`). As the MCP spec has evolved to include advanced capabilities such as `tools`, `resources`, `prompts`, `agentic behaviors`, `streaming`, and `authentication`, we are adapting MCP-DSL to match the full scope of the protocol.

MCP-DSL expresses these concepts in a clean, high-level language that supports workflows with:

* `model`: defines an AI capability
* `context`: holds evolving shared state
* `interaction`: connects models to context declaratively
* `tool`: invokes external functions/APIs
* `resource`: binds external data (e.g., documents, images)
* `prompt`: defines reusable prompt templates
* `agent`: coordinates multi-step plans and autonomous behavior
* `streaming`, `auth`, `capabilities`: protocol-level flags and metadata

➡️ [Read full breakdown and examples](./docs/core-concepts.md)

**Note:** MCP-DSL supports both `.mcp` files (strictly MCP-compatible) and `.mcpe` files (MCP-Extended) that introduce powerful constructs such as `agent`, `stateflow`, `retry`, `pattern`, and more.

Use `.mcpe` when defining rich workflows or domain-specific orchestration logic. Legacy tools expecting `.mcp` will safely ignore these extensions.

---

## 🗂️ Project Structure

```
mcp-dsl/
├── README.md                 # Vision & intro (this file)
├── LICENSE                   # MIT or your preferred license
├── .gitignore                # Standard for language tooling
│
├── grammar/                  # DSL grammar files (e.g., PEG.js / ANTLR)
├── parser/                   # Parsing and AST construction
├── ast/                      # AST data structures
├── codegen/                  # Code generators for various targets
├── cli/                      # Command-line interface tool
├── examples/                 # Example DSL files
├── runtime/                  # Runtime libraries for executing DSL
├── tests/                    # Unit tests for parser and codegen
└── docs/                     # Documentation and specifications
```

---

## 🛠️ Roadmap

* [x] Define PEG.js grammar (being transitioned to ANTLR grammar)
* [ ] Implement parser and AST builder
* [ ] Build code generators for Python and Rust
* [ ] Add support for additional language targets (Go, TypeScript, Kotlin, etc.) with idiomatic implementations
* [ ] Provide CLI and runtime engine
* [ ] Publish docs and examples

---

## 📚 Explore the Project

* [📜 MCP-DSL Manifesto](./docs/mcp-dsl-manifesto.md)
* [🧱 Core Concepts](./docs/core-concepts.md)
* [✍️ Syntax Design](./docs/syntax-design-notes.md)
* [⚙️ Language Architecture](./docs/language-design.md)
* [🔁 Common Patterns](./docs/patterns-library.md)
* [🧵 Async & Concurrency](./docs/concurrency-and-async.md)
* [🚧 Error Handling](./docs/error-handling.md)
* [🔬 Domain Extensions (e.g. bioinformatics)](./docs/domain-extensions.md)
* [🧠 Retrieval-Augmented Generation](./docs/rag-explainer.md)
* [🧰 Custom GPTs for MCP-DSL Authoring and Review](./docs/custom-gpt-setup.md)
* [💭 Issues and Challenges](./docs/issues-and-challenges.md)
* [🤝 How to Contribute](./docs/contributing.md)

---

## 📎 Grammar Definition

MCP-DSL is currently defined via ANTLR (with PEG.js legacy support being phased out).

➡️ [View full grammar and parser design notes](./docs/syntax-design-notes.md)

---

## 🤝 Join Us

If you're excited about shaping the future of AI tooling and interoperability, you're in the right place. We're actively building support for multi-language code generation — including Python, Rust, Go, and more — and welcome contributors with expertise or interest in any programming language.

---

## 📜 License

Open-source, MIT-style. Final license TBD based on community discussion.

---

> "When high-level and low-level constructs are forced to coexist, abstraction is begging to be born."

---

## ⚠️ Project Status: Paused — with Thanks, Lessons, and Open Doors

> **Note from the Author**
> This project began as a side exploration after encountering some overly complex or inelegant MCP server scaffolding. With the help of ChatGPT, I rapidly sketched out an ambitious vision: a domain-specific language (MCP-DSL) to declaratively describe model-context orchestration in a more readable, composable, and maintainable way.

Together with GPT, I was able to:

* Draft formal grammars and examples
* Explore language design patterns
* Map core MCP features to DSL constructs
* Reflect critically on syntax, semantics, and practical implementation pathways

However — and this is a mea culpa — **I hadn’t realized that the MCP specification had already evolved far beyond its initial form**. My early assumptions were based on an outdated snapshot of the protocol, and I underestimated the scope of changes that had since been incorporated.

> Continuing meaningfully would now require tight alignment with the current [official spec](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/schema/draft/schema.ts) and a shift in project direction — which goes beyond my available time and attention.

So I’ve chosen to pause here and leave the door open:

### ✅ If You’re Interested in This Space:

* Consider contributing directly to the [MCP project](https://github.com/modelcontextprotocol/modelcontextprotocol)
* Explore whether DSL-like constructs could aid **tooling**, **validation**, or **example generation**
* Fork, reuse, or remix this repo — everything here is shared in the spirit of exploration

This project was made possible in large part through ongoing collaboration with ChatGPT. Even if incomplete, it served as a catalyst for learning, critical thinking, and imagining new interfaces between people and protocol-driven AI.

— *\[John Majerus]*
