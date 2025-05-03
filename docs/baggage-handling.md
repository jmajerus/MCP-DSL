# Design Philosophy: Baggage Handling in MCP-DSL

In MCP-DSL, we embrace a pragmatic approach to commonly used fields and configurations that may not be formally interpreted by the DSL itself — but are nonetheless essential to the surrounding workflow.

We call this philosophy **baggage handling**: the idea that certain fields can and should be *carried* through the pipeline, even if MCP-DSL doesn’t act on them directly.

---

## ✈️ Why “Baggage Handling”?

Just like an airport doesn’t open your suitcase to decide whether you can board a plane, MCP-DSL doesn’t need to *use* every piece of data — but it can tag, route, and forward it.

This allows our DSL to:

* Be **friendly to real-world use cases**
* Avoid rejecting common, harmless metadata
* Support integration with downstream systems (docgen, visualization, packaging)

---

## ✅ What Kinds of Baggage Can Be Carried?

### ✅ Model Configuration Fields

```mcp
config ModelDetails {
  image_format: "jpeg,png"
  precision: "mixed_float16"
  tokenizer: "openai/unified"
  max_tokens: 8192
}
```

### ✅ Meta Fields

```mcp
meta {
  author: "SynthAI Labs"
  created: "2025-03-01"
  license: "Apache-2.0"
  tags: ["multimodal", "transformer"]
}
```

These fields may not influence protocol execution but can inform:

* Build pipelines
* Documentation
* Audit and reproducibility
* Deployment metadata

---

## 🧠 Benefits

* **Graceful compatibility** with model config formats already in the wild
* **Unified DSL**: possible to collapse `.mcpe` + `.mcp` into one file if desired
* **Future-proofing**: tools can add new fields without breaking DSL parsing
* **Easier GPT integration**: fewer rigid exclusions during synthesis

---

## 🚧 How It Works

* Unknown keys inside `meta` or `config` blocks are preserved as-is in the AST
* Tools can opt in to validate or enforce subsets
* Parsers are schema-aware, not schema-locked

---

## 🌐 Optional Convention: `@opaque` Blocks

If a block is meant to be carried but never interpreted, it can be flagged:

```mcp
@opaque
config downstream_only {
  image_resolution: "224x224"
  embedding_strategy: "shared-space"
}
```

---

## ✅ TL;DR

* We carry what’s common
* We forward what’s useful
* We parse what’s core
* We reject only what’s harmful

This makes MCP-DSL robust, compatible, and ready to coexist in the messy, modular world AI teams actually work in.
