# MCP-DSL: A Declarative Language for Model-Context Interaction

## 🌟 Vision
MCP-DSL is a domain-specific language (DSL) for expressing high-level model and context interaction logic in AI systems. It abstracts away low-level plumbing, enabling developers to describe intent clearly while generating reliable and maintainable backend code.

Whenever high-level orchestration logic is mixed with low-level implementation code, we lose clarity and composability. MCP-DSL separates these layers by giving AI developers a clean language to define:

- **Models** and their input/output types
- **Context containers** and their evolving state
- **Interactions** that connect models to context
- **Protocol rules** for state transitions and binding logic

## 💡 Why MCP-DSL?
- ✅ Declarative: Focus on *what* the model should do, not *how* to wire it
- ✅ Safe: Generate validated, structured, auditable code
- ✅ Composable: Reuse and combine model-context patterns
- ✅ Scalable: Add new models or interactions without breaking structure

## 🧱 Core Concepts
### `model`
Defines a functional model or AI capability.
```mcp
model Summarizer {
  input: text: String
  output: summary: String
}
```

### `context`
Defines persistent state shared across model invocations.
```mcp
context Session {
  user: User
  lastSummary: String?
}
```

### `interaction`
Describes how a model is used and how its output updates context.
```mcp
interaction summarize(text: String) -> Session {
  use Summarizer
  bind output.summary to Session.lastSummary
}
```

## 🗂️ Project Structure
```
mcp-dsl/
├── README.md                 # Vision & intro (this file)
├── LICENSE                   # MIT or your preferred license
├── .gitignore                # Standard for language tooling
│
├── grammar/                  # DSL grammar files (e.g., PEG.js)
│   └── mcp_grammar.pegjs     # PEG.js grammar definition
│
├── parser/                   # Parsing and AST construction
│   └── parser.js             # PEG parser loader and AST builder
│
├── ast/                      # AST data structures
│   └── nodes.js              # Classes for DSL node representation
│
├── codegen/                  # Code generators for various targets
│   ├── python_generator.js   # Python code generator
│   └── rust_generator.rs     # Optional: Rust backend
│
├── cli/                      # Command-line interface tool
│   └── mcp_cli.js            # Entry point CLI
│
├── examples/                 # Example DSL files
│   ├── simple_summarizer.mcp
│   └── login_flow.mcp
│
├── runtime/                  # Runtime libraries for executing DSL
│   └── python/               # Python runtime (context, models)
│
├── tests/                    # Unit tests for parser and codegen
│   └── test_parser.js
│
└── docs/                     # Documentation and specifications
    └── syntax.md             # Formal syntax guide and examples
```

## 🛠️ Roadmap
- [x] Define PEG.js grammar
- [ ] Implement parser and AST builder
- [ ] Build code generators for Python and Rust
- [ ] Provide CLI and runtime engine
- [ ] Publish docs and examples

## 🤝 Join Us
If you're passionate about making AI orchestration safer, clearer, and more elegant, you're in the right place. Contributions, ideas, and feedback are all welcome.

## 📜 License
Open-source, MIT-style. Final license TBD based on community discussion.

---

> "When high-level and low-level constructs are forced to coexist, abstraction is begging to be born."

---

### 📎 Grammar: `grammar/mcp_grammar.pegjs`
```pegjs
Start
  = Statement*

Statement
  = ModelDecl / ContextDecl / InteractionDecl

ModelDecl
  = "model" _ name:Identifier _ "{" _ ModelFields _ "}"

ModelFields
  = field:(InputField / OutputField)*

InputField
  = "input:" _ name:Identifier ":" _ Type

OutputField
  = "output:" _ name:Identifier ":" _ Type

ContextDecl
  = "context" _ name:Identifier _ "{" _ ContextFields _ "}"

ContextFields
  = (Identifier ":" _ Type)*

InteractionDecl
  = "interaction" _ Identifier "(" _ ArgList _ ")" _ "->" _ Identifier _ "{" _ InteractionBody _ "}"

InteractionBody
  = (UseStmt / BindStmt)*

UseStmt
  = "use" _ Identifier

BindStmt
  = "bind" _ Path _ "to" _ Path

ArgList
  = (Identifier ":" _ Type)*

Type
  = Identifier

Path
  = Identifier ("." Identifier)*

Identifier
  = [a-zA-Z_][a-zA-Z0-9_]*

_ "whitespace"
  = [ \t\n\r]*
```

