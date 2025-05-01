const fs = require("fs");
const path = require("path");
const peg = require("pegjs");

// Load the grammar source
const grammarPath = path.join(__dirname, "../grammar/mcp_grammar.pegjs");
const grammarSource = fs.readFileSync(grammarPath, "utf8");

// Build the parser from grammar
const parser = peg.generate(grammarSource);

/**
 * Parse an MCP DSL file into an abstract syntax tree (AST)
 * @param {string} source - Raw MCP DSL code as a string
 * @returns {object} Parsed AST
 */
function parseMCP(source) {
  try {
    return parser.parse(source);
  } catch (e) {
    console.error("Parse error:", e.message);
    throw e;
  }
}

// CLI entry point for testing
if (require.main === module) {
  const inputPath = process.argv[2];
  if (!inputPath) {
    console.error("Usage: node parser.js <file.mcp>");
    process.exit(1);
  }

  const code = fs.readFileSync(inputPath, "utf8");
  const ast = parseMCP(code);
  console.log(JSON.stringify(ast, null, 2));
}

module.exports = {
  parseMCP,
};
