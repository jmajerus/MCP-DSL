mod ast;
use askama::Template;
use ast::{Context, Interaction, Model};
use std::fs;

#[derive(Template)]
#[template(path = "python_class.j2")]
struct PythonTemplate<'a> {
    models: &'a [Model],
    contexts: &'a [Context],
    interactions: &'a [Interaction],
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let json = fs::read_to_string("example_ast.json")?;
    let value: serde_json::Value = serde_json::from_str(&json)?;

    let models: Vec<Model> = serde_json::from_value(value["models"].clone())?;
    let contexts: Vec<Context> = serde_json::from_value(value["contexts"].clone())?;
    let interactions: Vec<Interaction> = serde_json::from_value(value["interactions"].clone())?;

    let template = PythonTemplate {
        models: &models,
        contexts: &contexts,
        interactions: &interactions,
    };

    let output = template.render()?;
    println!("{}", output);

    Ok(())
}
