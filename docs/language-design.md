# Language Design Notes for MCP-DSL

This document outlines considerations and potential extensions to the core MCP-DSL syntax and semantics, anticipating future needs and broader adoption. While the current MCP primitives (`model`, `context`, `interaction`) provide a strong foundation, this design document explores how the DSL might evolve to support more advanced use cases.

## 🔧 Existing Primitives
- `model`: Defines a callable function, AI model, or transformation unit
- `context`: Holds persistent, updatable state across interactions
- `interaction`: Describes model invocation and how its output updates context

## 🧱 Candidate Primitives for Future Inclusion

### `agent`
Encapsulates autonomous behavior with goals, plans, and persistent internal state. Useful for agent-based systems, assistants, or multistep orchestration.

```mcp
agent Researcher {
  goal: enrich query with citations
  context: Session
  plan:
    - interaction: retrieve
    - interaction: synthesize
}
```

### `stateflow`
Encodes state transitions in a context, similar to finite state machines. Ideal for protocols, auth flows, or UI step management.

```mcp
stateflow Session {
  state: unauthenticated -> authenticated on login
  state: authenticated -> expired on timeout
}
```

### `validate`
Specifies runtime constraints or input schema rules.

```mcp
validate email: isValidEmail
```

### `chain`
Groups multiple interactions or subroutines into a reusable unit.

```mcp
chain build_response(query: String) -> Session {
  steps:
    - retrieve
    - summarize
    - refine
}
```

### `resource`
Declares external data or tools needed by the system.

```mcp
resource vectorStore: Pinecone
resource calendarAPI: HTTP
```

### `event`
Declares system or external triggers that initiate actions.

```mcp
event onNewDocument -> interaction ingestDoc
```

## 🌐 Forward Compatibility
- Reserve likely keywords for future use
- Allow per-interaction metadata (e.g. `@async`, `@batch`, `@secure`)
- Enable versioning for grammar or context modules
- Support extensions via `@experimental` blocks

## 🤝 Coordination with Anthropic
Since Anthropic is the official steward of the MCP standard, proposals for additions or syntax extensions should be coordinated thoughtfully. Our approach assumes:

- This project aims to remain aligned with the spirit of the standard
- Any extensions will be designed for graceful fallback or modular opt-in
- When stable, suggestions may be proposed for upstream discussion or community review

## 📍 Next Steps
- Track current prototype usage patterns to inform priority of primitives
- Add sample `.mcp` files for each candidate feature
- Annotate experimental grammar separately for each construct

