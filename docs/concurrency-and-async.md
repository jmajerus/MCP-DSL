# Concurrency and Asynchronous Patterns in MCP-DSL

As MCP-DSL matures into a protocol for orchestrating model-context interactions in real-world systems, it must support patterns commonly found in distributed and asynchronous environments. This document outlines proposed syntax and semantics for expressing concurrency, deferred execution, and asynchronous event handling.

---

## 🕒 Motivation
Modern AI agents and applications often require:
- Running multiple models or tools in parallel
- Awaiting asynchronous inputs (e.g., file uploads, human-in-the-loop)
- Delaying or deferring parts of a workflow
- Persisting workflows across sessions or system restarts

---

## ✅ Proposed Features

### `@async` Annotation
Marks an interaction as asynchronous. Indicates that the caller should not expect an immediate result, and that completion may be handled via a continuation, event, or message.

```mcp
@async
interaction analyzeLargeFile(fileId: String) -> Session {
  use FileAnalyzer
  bind output.result to Session.lastAnalysis
}
```

---

### `fork` / `join` Blocks
Enables parallel execution of models or substeps within a single interaction. Forked steps run independently and populate shared context. `join` blocks consume all intermediate results.

```mcp
interaction buildResponse(query: String) -> Session {
  fork {
    use Retriever
    bind output.docs to Session.docs
  }

  fork {
    use QueryClassifier
    bind output.intent to Session.intent
  }

  join {
    use AnswerComposer
    bind input.docs to Session.docs
    bind input.intent to Session.intent
    bind output.response to Session.answer
  }
}
```

---

### Agent Plans with Wait/Trigger Support *(planned)*
Agents can include `wait`, `on`, or `event` triggers that pause plan execution until some condition is met.

```mcp
agent AutoResponder {
  goal: respond to user input with refinement
  context: Session
  plan:
    - wait on event: userMessage
    - interaction: askFAQ
    - wait on event: userFeedback
    - interaction: refineResponse
}
```

---

## 🧠 Design Principles
- All concurrency constructs remain **declarative** and do not assume threading models
- Runtime environments may map `fork`/`join` to futures, threads, or async calls
- Context is the shared medium between concurrent units
- Failures in forks can be caught or allowed to propagate

---

## 🔮 Future Work
- `timeout` or `retry` support per forked step
- Optional dependency chaining via `wait for` or `after`
- Execution graphs visualized from `fork`/`join`/`wait` blocks

---

By allowing declarative expression of asynchronous and concurrent behavior, MCP-DSL empowers developers to orchestrate complex workflows without sacrificing clarity or control.

