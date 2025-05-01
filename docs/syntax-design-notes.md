# MCP-DSL Syntax Design Notes

This document outlines proposed refinements to the MCP-DSL syntax to improve readability, ease of parsing, and user experience. These are designed to maintain backwards compatibility while offering more expressive and developer-friendly syntax.

---

## ✅ Comma-Separated Fields
Allow commas between field declarations in `model` and `context` blocks.

### Before:
```mcp
model Summarizer {
  input: text: String
  output: summary: String
}
```

### After (Option A):
```mcp
model Summarizer {
  input: text: String,
  output: summary: String,
}
```

### After (Option B - Nested):
```mcp
model Summarizer {
  input {
    text: String,
  },
  output {
    summary: String,
  }
}
```

---

## ✅ Optional Semicolons
Permit optional semicolons at the end of individual statements (`use`, `bind`, `validate`).

```mcp
bind output.answer to Session.lastAnswer;
```

---

## ✅ Named Parameters Format (Alternative `interaction` Syntax)
Provides a clearer structure with explicit block scoping for `input`, `output`, and `body`.

```mcp
interaction askFAQ {
  input: question: String,
  output: Session,
  body: {
    use FAQRetriever;
    bind input.question to question;
    bind output.answer to Session.lastAnswer;
  }
}
```

---

## ✅ Block-Based Clause Grouping
Support optional block-style grouping for `use`, `bind`, `validate` sections.

```mcp
interaction askFAQ {
  input: question: String,
  output: Session,

  use {
    FAQRetriever
  },

  bind {
    input.question to question,
    output.answer to Session.lastAnswer
  }
}
```

---

## ✅ Comment Support
Support inline and block comments for DSL documentation.

```mcp
/// Stores last user query and answer
context Session {
  user: User,  // system identity
  lastQuestion: String,
  lastAnswer: String
}
```

---

## 🛠️ Implementation Plan
- Phase 1: Add comma and semicolon support (trivial ANTLR updates)
- Phase 2: Enable nested blocks for `input` and `output`
- Phase 3: Add comment parsing (`//`, `///`)
- Phase 4: Explore alternative `interaction` block structure as an opt-in

---

These refinements aim to support clearer authoring, tool integration, and eventual IDE/linter enhancements.

