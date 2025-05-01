# Pre-Coordinated Patterns in MCP-DSL

This document outlines reusable, pre-coordinated syntax patterns for common AI orchestration scenarios in MCP-DSL. These patterns elevate intent, reduce boilerplate, and give the DSL a "smart fit" for common problems — going beyond general-purpose languages.

---

## 🔁 Retry with Backoff
Automatically retry a model call with optional exponential delay.

```mcp
retry 3 {
  use FastModel
  bind output.result to Session.result
}
catch {
  use ReliableBackupModel
  bind output.result to Session.result
}
```

---

## 🚦 Guarded Execution
Branch interaction logic based on context or prior results.

```mcp
guard Session.user.role == "admin" then {
  use AdminSummaryGenerator
}
else {
  use PublicSummaryGenerator
}
```

---

## 🌐 Fanout + Merge
Call multiple models/sources in parallel and merge their outputs.

```mcp
fanout {
  use ProductDB
  use KnowledgeBase
  use WebSearch
}
merge outputs into Session.matches
```

---

## ⏳ Await / Polling
Pause flow until a specific external event or timeout.

```mcp
await event userConfirmed(timeout: 5m) then {
  use ProceedWithOnboarding
}
else {
  use CancelWorkflow
}
```

---

## 🔉 Debounce / Throttle
Avoid repeated model use during burst input.

```mcp
use SearchEngine debounce 1s
bind output.results to Session.results
```

---

## 🧾 Scoped Logging
Automatically wrap an interaction with logging or audit trail.

```mcp
@log_scope("PII trace")
interaction processSensitiveData {
  use Anonymizer
  bind output.cleaned to Session.cleaned
}
```

---

## 🔄 Lifecycle Hooks
Execute logic before or after a model is used within an interaction.

```mcp
interaction registerUser(email: String) -> Session {
  before {
    use EmailNormalizer
    bind output.email to email
  }
  use UserRegistrar
  after {
    use WelcomeMailer
    bind input.email to email
  }
}
```

---

## 🔮 Future Directions
- Allow `pattern` blocks to be declared and reused by name
- Support `@pattern` annotation for code generation clarity
- Introduce standardized macro expansion rules

These patterns aim to make MCP-DSL not just a protocol language, but a toolkit for expressing resilient, expressive, and intention-aligned workflows.

