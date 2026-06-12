# Software Design Lab Report Resource Pack

This minimal pack contains the reusable pieces for the Chinese software design pattern lab workflow.

## Contents

- `skill/SKILL.md`
  The Codex skill instructions.
- `skill/agents/openai.yaml`
  UI metadata for the skill.
- `templates/cover-template-midterm.docx`
  The school-style cover/template used for reports.
- `references/AGENTS.md`
  Coursework diagram and hand-finished report rules.
- `scripts/generate_docx_template.py`
  A small reusable starter for generating a DOCX report from the cover template.

## How To Install The Skill

Copy the `skill` folder into your Codex skills directory and rename it:

```bash
mkdir -p ~/.codex/skills/software-design-lab-report
cp -R skill/* ~/.codex/skills/software-design-lab-report/
```

## How To Use The Template

Use `templates/cover-template-midterm.docx` as the DOCX base. The generator keeps the cover layout and removes the old body before appending new report content.

The generated lab folder should still include code, diagrams, screenshots, and a final DOCX under `output/doc/`.
