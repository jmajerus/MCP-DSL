# Retrieval-Augmented Generation (RAG) in MCP-DSL

Retrieval-Augmented Generation (RAG) is a technique for enhancing language model outputs by grounding them in external knowledge retrieved at runtime. It combines a retriever model (which searches relevant documents) with a generator model (which synthesizes a response).

MCP-DSL offers a clean, declarative way to express this architecture:

## 🧠 Why Use RAG
- Ground LLM outputs in up-to-date, factual context
- Reduce hallucinations
- Enable domain-specific knowledge injection
- Separate retrieval and reasoning concerns

## 🧱 RAG in MCP-DSL
Using the MCP-DSL `model`, `context`, and `interaction` primitives, a typical RAG pipeline might be represented like this:

```mcp
interaction retrieve_and_answer(query: String) -> Session {
  use Retriever
  bind output.documents to Session.relevantDocs

  use AnswerGenerator
  bind input.query to query
  bind input.context to Session.relevantDocs
  bind output.answer to Session.lastAnswer
}
```

### Components:
- **Retriever**: Takes a query and returns a ranked list of relevant `TextChunk`s.
- **AnswerGenerator**: Consumes the original query and retrieved context to generate a final answer.
- **Context (Session)**: Stores intermediate and final outputs such as `relevantDocs` and `lastAnswer`.

## 📦 Benefits of Expressing RAG with MCP-DSL
- Declarative and testable
- Readable protocol design
- Clean separation of model roles
- Pluggable models (swap in any retriever or generator)

## 🔮 Future Enhancements
- `top_k` or filtering annotations on bindings
- Looping over multiple chunks
- Agent-style iterative refinement of answers

By supporting RAG natively in its syntax and structure, MCP-DSL allows developers to scale up AI workflows with transparency, modularity, and rigor.

See `examples/rag_search_example.mcp` for a working reference.

