# AGENTS.md

## Purpose

This repository contains coursework-style software design materials. When helping with reports, UML, and pattern diagrams, optimize for clarity, teachability, and believable hand-finished output rather than maximum automation.

## Diagram Rules For Coursework

### 1. Prefer "teaching diagrams" over "complete dependency dumps"

- A coursework UML diagram should explain one idea clearly.
- Do not put every inheritance, dependency, and creation relation into one diagram.
- If an auto-generated graph starts to look like a spider web, the diagram is wrong for the assignment even if the relations are technically correct.

### 2. Split diagrams by intent

For design-pattern assignments, separate diagrams by purpose:

- Pattern structure diagram:
  Show the standard roles of the pattern itself.
- Program main-structure diagram:
  Show only the core classes used in the implementation.
- Appearance/theme-change diagram:
  Show only the classes relevant to UI/theme switching.

Do not merge all three goals into one graph.

### 3. Abstract Factory structure diagram expectations

When the assignment asks for "Abstract Factory pattern structure diagram", it usually means the standard template roles:

- `Client`
- `AbstractFactory`
- `ConcreteFactory1`, `ConcreteFactory2`
- `AbstractProductA`, `AbstractProductB`
- `ProductA1`, `ProductA2`, `ProductB1`, `ProductB2`

The core idea to express is:

- Client depends on abstract factory and abstract products.
- Each concrete factory produces a matching family of products.

For coursework, the minimal clear version is usually enough:

- Keep inheritance/implementation relations.
- Keep client-to-abstraction dependencies.
- Add concrete-factory-to-product creation relations only if they improve explanation.
- Avoid drawing every possible dependency if it harms readability.

### 4. Mermaid usage best practices

- Treat Mermaid as a layout starter, not the final UML authority.
- Prefer simple `direction TB` or `direction LR`.
- Reduce relation count before trying to "fix" layout.
- If Mermaid produces a tangled graph, simplify the model first instead of adding more syntax.
- Use draw.io after import for final human cleanup.

### 5. draw.io workflow

Recommended workflow for coursework:

1. Draft the structure in Mermaid.
2. Import into draw.io via `Arrange -> Insert -> Mermaid...`.
3. Convert it into a hand-finished submission by manually adjusting:
   - box positions
   - connector bends
   - titles
   - grouping areas
4. Export images or PDF from draw.io as the final deliverable.

### 6. Hand-finished look requirements

To preserve believable manual effort:

- Move several nodes by hand after import.
- Do not keep perfect symmetry in every diagram.
- Use different layouts across diagrams when appropriate.
- Add light grouping boxes such as:
  - "抽象工厂层"
  - "具体工厂层"
  - "抽象产品层"
  - "具体产品层"
- Keep titles in Chinese when the report is in Chinese.

### 7. Assignment-oriented priority order

When there is a tradeoff, prioritize in this order:

1. The diagram is easy for a teacher to read quickly.
2. The diagram matches the assignment wording.
3. The diagram looks plausibly hand-organized.
4. The diagram is formally complete.

Formal completeness is not the top priority if it makes the coursework diagram harder to understand.

