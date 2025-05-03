# MCP-DSL Preprocessing and Routing

To support a scalable, domain-aware ecosystem without requiring numerous file extensions, MCP-DSL files adopt a standardized **metadata header block**. This enables routing, validation, and grammar selection **before parsing the body** of the DSL file.

---

## 📌 Why This Matters

* Enables **domain-aware tooling** without depending on file extensions
* Allows **versioned grammar selection**
* Supports **clear, self-documenting workflows**
* Makes `.mcpe` files truly composable and multi-purpose

---

## ✅ Required Header Metadata

Each `.mcpe` file must begin with a standardized comment block:

```mcp
// MCP-DSL File
// @domain: bioinformatics
// @grammar: mcpb-1.0
// @version: 0.3
```

| Field      | Purpose                                   |
| ---------- | ----------------------------------------- |
| `@domain`  | Declares the logical domain of the file   |
| `@grammar` | Specifies the grammar variant and version |
| `@version` | Indicates the DSL file format version     |

This metadata is **machine-readable and mandatory**.

---

## ⚙️ Preprocessor Responsibilities

A CLI tool or build system should:

1. **Read only the header block** (first few lines)
2. Validate required fields are present
3. Use `@grammar` to select the correct parser/validator
4. Optionally warn if the declared `@domain` and `@grammar` don’t match known conventions
5. Optionally inject the metadata into downstream processing or documentation

---

## 📦 CLI Tool Example

```bash
mcp compile myfile.mcpe
```

Would result in:

```text
> Domain: bioinformatics
> Grammar: mcpb-1.0
> Routing to parser: grammar/mcpb.mcpg
> Validating syntax...
> Compiling to Python target...
```

---

## 🚫 Fallbacks & Errors

| Scenario                            | Behavior                              |
| ----------------------------------- | ------------------------------------- |
| Missing `@grammar`                  | ❌ Reject with message                 |
| Unknown grammar                     | ⚠️ Warn or error based on strict mode |
| Mismatched grammar vs. file content | ⚠️ Flag but allow manual override     |
| Deprecated grammar version          | ⚠️ Notify of preferred upgrade path   |

---

## 🧠 Future Extensions

* `@depends` or `@imports` fields to pre-resolve module dependencies
* `@target: rust` to hint backend codegen
* `@license` to support open model documentation

---

This preprocessing step gives MCP-DSL the rigor of a typed language, the portability of Markdown, and the contextual richness of domain-specific pipelines — all while keeping syntax clean and extensible.
