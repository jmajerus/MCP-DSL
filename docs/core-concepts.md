# Core Concepts in MCP-DSL

### 🧩 `model`
Defines an atomic AI capability — typically a function, tool, or black-box model with defined inputs and outputs. Models are the basic computational units of MCP-DSL.

```mcp
model Summarizer {
  input: text: String
  output: summary: String
}
```

---

### 🧠 `context`
Defines persistent, evolving state that spans multiple model invocations. It holds what the system “remembers” or tracks across interactions — often user sessions, task states, or environments.

```mcp
context Session {
  user: User
  lastSummary: String?
}
```

---

### 🔄 `interaction`
Describes a single use of one or more models in context, with declarative bindings from outputs to state. Interactions are the primary unit of orchestration.

```mcp
interaction summarize(text: String) -> Session {
  use Summarizer
  bind output.summary to Session.lastSummary
}
```

---

### 🔗 `bind`
Specifies how values returned by a model are assigned to fields within a context. A `bind` can express both shallow and nested updates.

```mcp
bind output.email to Session.user.email
```

---

### 🛡 `validate` *(planned)*
Declares constraints on interaction inputs using reusable validators. Helps ensure clean, fail-fast behavior across protocols.

```mcp
interaction register(email: String) -> Session {
  validate email: isValidEmail
  use AccountCreator
  bind output.user to Session.user
}
```

---

### 🧭 `stateflow` *(planned)*
Enables state transition modeling within a context — useful for workflows like onboarding, authentication, or game state.

```mcp
stateflow Session {
  state: unauthenticated -> authenticated on login
  state: authenticated -> expired on timeout
}
```

---

### 👤 `agent` *(future extension)*
Defines autonomous, persistent actors that manage their own goals and sub-interactions, coordinating model and context usage over time.

```mcp
agent ResearchAssistant {
  goal: summarize and tag new documents
  context: Session
  plan:
    - interaction: summarize
    - interaction: tagSummary
}
```

---

### 📦 `import` *(planned)*
Allows reuse of models, contexts, and agents from external modules.

```mcp
import auth from "auth.mcp"
import Session from "common/session.mcp"
```

---

### 📝 `///` Doc Comments *(planned)*
Comments can be added directly in MCP-DSL for use in auto-generated documentation.

```mcp
/// This interaction summarizes user input and stores the result.
interaction summarize(text: String) -> Session { ... }
```

