from parser.MCPVisitor import MCPVisitor
from parser.MCPParser import *

class ASTBuilder(MCPVisitor):
    def __init__(self):
        self.models = []
        self.contexts = []
        self.interactions = []

    def visitProg(self, ctx: MCPParser.ProgContext):
        for stmt in ctx.statement():
            self.visit(stmt)
        return {
            "models": self.models,
            "contexts": self.contexts,
            "interactions": self.interactions
        }

    def visitModelDecl(self, ctx: MCPParser.ModelDeclContext):
        name = ctx.IDENTIFIER().getText()
        inputs = []
        outputs = []
        for field in ctx.modelField():
            label = field.getChild(0).getText()
            fname = field.IDENTIFIER().getText()
            ftype = field.type_().getText()
            if label == "input:":
                inputs.append({"name": fname, "field_type": ftype})
            else:
                outputs.append({"name": fname, "field_type": ftype})
        self.models.append({"name": name, "inputs": inputs, "outputs": outputs})

    def visitContextDecl(self, ctx: MCPParser.ContextDeclContext):
        name = ctx.IDENTIFIER().getText()
        fields = []
        for f in ctx.contextField():
            fname = f.IDENTIFIER().getText()
            ftype = f.type_().getText()
            fields.append({"name": fname, "field_type": ftype})
        self.contexts.append({"name": name, "fields": fields})

    def visitInteractionDecl(self, ctx: MCPParser.InteractionDeclContext):
        name = ctx.IDENTIFIER(0).getText()
        return_type = ctx.IDENTIFIER(1).getText()
        args = []
        body = []

        if ctx.argList():
            for arg in ctx.argList().argument():
                arg_name = arg.IDENTIFIER(0).getText()
                arg_type = arg.type_().getText()
                args.append({"name": arg_name, "field_type": arg_type})

        for stmt in ctx.interactionBody():
            if stmt.useStmt():
                model = stmt.useStmt().IDENTIFIER().getText()
                body.append({"type": "Use", "model_name": model})
            if stmt.bindStmt():
                from_path = stmt.bindStmt().path(0).getText()
                to_path = stmt.bindStmt().path(1).getText()
                body.append({"type": "Bind", "from": from_path, "to": to_path})

        self.interactions.append({
            "name": name,
            "args": args,
            "return_type": return_type,
            "body": body
        })
