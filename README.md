# MCP-DSL: A Declarative Language for Model-Context Interaction

## 🌟 Vision

MCP-DSL is a domain-specific language (DSL) for expressing high-level model and context interaction logic in AI systems. It abstracts away low-level plumbing, enabling developers to describe intent clearly while generating reliable and maintainable backend code.

Whenever high-level orchestration logic is mixed with low-level implementation code, we lose clarity and composability. MCP-DSL separates these layers by giving AI developers a clean language to define:

* **Models** and their input/output types
* **Context containers** and their evolving state
* **Interactions** that connect models to context
* **Protocol rules** for state transitions and binding logic

## 💡 Why MCP-DSL?

* ✅ Declarative: Focus on *what* the model should do, not *how* to wire it
* ✅ Safe: Generate validated, structured, auditable code
* ✅ Composable: Reuse and combine model-context patterns
* ✅ Scalable: Add new models or interactions without breaking structure


## 🧱 Core Concepts

MCP-DSL builds upon the principles of the [Model-Context Protocol (MCP)](https://github.com/anthropics/mcp), extending them into a fully declarative domain-specific language.

While MCP provides a structured way for tools and models to coordinate via messaging, MCP-DSL expresses those flows as readable, composable, and traceable declarations.

At its core, MCP-DSL retains the original MCP entities:

- `model`: defines an AI capability
- `context`: holds evolving shared state
- `interaction`: connects models to context declaratively

➡️ [Read full breakdown and examples](./docs/core-concepts.md)

**Note:** MCP-DSL supports both `.mcp` files (strictly MCP-compatible) and `.mcpe` files (MCP-Extended) that introduce powerful constructs such as `agent`, `stateflow`, `retry`, `pattern`, and more.

Use `.mcpe` when defining rich workflows or domain-specific orchestration logic. Legacy tools expecting `.mcp` will safely ignore these extensions.

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

## 🗂️ Project Structure




## 🛠️ Roadmap

* [x] Define PEG.js grammar (being transitioned to ANTLR grammar)
* [ ] Implement parser and AST builder
* [ ] Build code generators for Python and Rust
* [ ] Add support for additional language targets (Go, TypeScript, Kotlin, etc.) with idiomatic implementations
* [ ] Provide CLI and runtime engine
* [ ] Publish docs and examples

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
* [💭 Issues and Challenges](./docs/issues-and-challenges.md)
* [🤝 How to Contribute](./docs/contributing.md)

## 📎 Grammar Definition

MCP-DSL is currently defined via ANTLR (with PEG.js legacy support being phased out).

➡️ [View full grammar and parser design notes](./docs/syntax-design-notes.md)

## 🤝 Join Us

If you're excited about shaping the future of AI tooling and interoperability, you're in the right place. We're actively building support for multi-language code generation — including Python, Rust, Go, and more — and welcome contributors with expertise or interest in any programming language.

## 📜 License

Open-source, MIT-style. Final license TBD based on community discussion.

---

> "When high-level and low-level constructs are forced to coexist, abstraction is begging to be born."
