# MCP Alignment: Mapping MCP-DSL to the Model Context Protocol

This document tracks how features in the MCP-DSL align with the evolving [Model Context Protocol (MCP)](https://github.com/anthropics/mcp). It helps ensure that DSL constructs remain compatible with the official specification while surfacing opportunities for innovation, extension, or graceful divergence.

---

## 🧱 Core Entities

| MCP Concept   | DSL Construct | Notes                     |
| ------------- | ------------- | ------------------------- |
| `model`       | `model`       | Supported natively in DSL |
| `context`     | `context`     | Supported natively        |
| `interaction` | `interaction` | Supported natively        |

---

## 🛠️ Tool Use and Invocation

| MCP Concept  | DSL Construct                 | Notes                                                       |
| ------------ | ----------------------------- | ----------------------------------------------------------- |
| `tool`       | `use ToolName`, `tool` blocks | DSL supports invocation and optional binding of tool output |
| `parameters` | `with` clause or arguments    | DSL supports tool parameterization                          |
| `response`   | `bind output to`              | DSL supports binding tool response to context or output     |

---

## 📄 Resource Management

| MCP Concept         | DSL Construct                | Notes                                                |
| ------------------- | ---------------------------- | ---------------------------------------------------- |
| `resource`          | `resource`, `import`, `load` | DSL supports reference or binding of structured data |
| `document`, `image` | format hints, MIME tags      | Supported or preserved in config blocks              |

---

## 💬 Prompt Templates

| MCP Concept | DSL Construct                   | Notes                                                        |
| ----------- | ------------------------------- | ------------------------------------------------------------ |
| `prompt`    | `prompt`, `template`, `pattern` | DSL supports reusable prompt templates and guidance wrappers |

---

## 🔁 Streaming and Feedback

| MCP Concept | DSL Construct                           | Notes                                          |
| ----------- | --------------------------------------- | ---------------------------------------------- |
| `streaming` | `@streaming`, `output: stream<String>`  | Annotated or typed in DSL                      |
| `progress`  | `bind progress to context`, `@progress` | Optional feature for long-running interactions |

---

## 🔐 Authentication and Authorization

| MCP Concept      | DSL Construct               | Notes                                                |
| ---------------- | --------------------------- | ---------------------------------------------------- |
| `auth`, `apikey` | `@secure`, `requires_token` | Planned future syntax; config pass-through supported |
| `scopes`         | config metadata             | Can be preserved via baggage handling                |

---

## 📡 Transport and Protocols

| MCP Concept           | DSL Construct                  | Notes                                                       |
| --------------------- | ------------------------------ | ----------------------------------------------------------- |
| `stdio`, `http`, `ws` | `transport:`, metadata headers | DSL does not enforce but allows config routing via metadata |
| `sse`, `websocket`    | passthrough via `meta` block   | Ignored by parser, respected by tooling                     |

---

## 🧠 Agentic Behavior

| MCP Concept     | DSL Construct                                | Notes                                               |
| --------------- | -------------------------------------------- | --------------------------------------------------- |
| `agent`, `plan` | `agent`, `plan`, `loop`, `retry`, `fallback` | DSL supports autonomous or reactive planning blocks |
| `delegation`    | `call`, `await`, `stateflow`                 | Modeled explicitly in DSL                           |

---

## 🚨 Error Handling and Reporting

| MCP Concept               | DSL Construct                                             | Notes                          |
| ------------------------- | --------------------------------------------------------- | ------------------------------ |
| `error`, `status`, `logs` | `try/catch/finally`, `log_scope`, `bind error to context` | Declarative support in `.mcpe` |

---

## 🚧 Capability Negotiation

| MCP Concept    | DSL Construct                                         | Notes                                               |
| -------------- | ----------------------------------------------------- | --------------------------------------------------- |
| `capabilities` | Planned support via `@requires`, metadata annotations | Will be expressed via conditionals or profile hints |

---

## ✅ Summary

MCP-DSL supports or anticipates nearly all evolving MCP features through:

* Explicit syntax constructs (e.g. `agent`, `tool`, `streaming`)
* Metadata and config pass-through (“baggage handling”)
* Declarative flow design compatible with agentic behavior

This alignment allows MCP-DSL to serve both as an authoring interface and a compiler frontend for robust, structured MCP applications.

➡️ Future versions of this document will include specific `.mcpe` examples per row above.
