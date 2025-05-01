class ModelNode {
    constructor(name, inputs = [], outputs = []) {
      this.type = "Model";
      this.name = name;
      this.inputs = inputs;
      this.outputs = outputs;
    }
  }
  
  class Field {
    constructor(name, fieldType) {
      this.name = name;
      this.fieldType = fieldType;
    }
  }
  
  class ContextNode {
    constructor(name, fields = []) {
      this.type = "Context";
      this.name = name;
      this.fields = fields;
    }
  }
  
  class InteractionNode {
    constructor(name, args = [], returnType = null, body = []) {
      this.type = "Interaction";
      this.name = name;
      this.args = args;
      this.returnType = returnType;
      this.body = body;
    }
  }
  
  class UseStatement {
    constructor(modelName) {
      this.type = "Use";
      this.modelName = modelName;
    }
  }
  
  class BindStatement {
    constructor(from, to) {
      this.type = "Bind";
      this.from = from;
      this.to = to;
    }
  }
  
  module.exports = {
    ModelNode,
    ContextNode,
    InteractionNode,
    UseStatement,
    BindStatement,
    Field,
  };
  