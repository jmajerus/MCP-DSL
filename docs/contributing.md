# Contributing to MCP-DSL

Thank you for your interest in contributing to MCP-DSL — a language for defining model-context interactions cleanly and portably across programming environments. We're building this tool to be useful, elegant, and inclusive.

## 🔧 Areas Where You Can Help
Whether you're a systems thinker, a language enthusiast, or just curious, there's a place for you here. Contributions are welcome in:

### 🧠 Language Design
- Propose syntax refinements
- Help with semantic rule definitions
- Expand the DSL to cover more use cases

### 🏗️ Backend Code Generators
We aim to support multiple languages:
- Python
- Rust
- Go
- TypeScript / JavaScript
- Kotlin
- C++
- Java

Each backend needs:
- Language-specific templates
- Output validators
- Style compliance helpers (formatters, linters)

### 🧪 Testing & Examples
- Add `.mcp` examples that cover corner cases
- Write integration tests that compare AST to generated code
- Provide before/after examples for generator targets

### 🧰 Tooling & Infrastructure
- Improve CLI tools and developer experience
- Integrate linting, formatting, and CI workflows
- Help package language-specific runtimes

### 📚 Documentation & Outreach
- Help with user guides and examples
- Write docs for a specific language target
- Share tutorials or demos

## 🛠️ Getting Started
1. Fork this repo and clone it locally
2. Run `python main.py examples/example.mcp` to generate AST
3. Explore or add to the generator in your language of choice
4. Run tests or create new ones

We recommend using virtual environments (Python) or language-specific build tools (e.g., `cargo`, `go mod`, `npm`) to isolate dependencies.

## 🤝 Code of Conduct
We expect respectful collaboration and open dialogue. This project is for everyone.

## 📬 Questions? Suggestions?
Open an issue or discussion thread — we welcome feedback at all levels.

---
Let’s build something powerful, elegant, and truly cross-language — together.

