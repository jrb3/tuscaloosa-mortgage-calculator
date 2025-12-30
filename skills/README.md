# Claude Code Skills

This directory contains custom skill files for Claude Code. Skills are reusable tools that extend Claude Code's capabilities for project-specific tasks.

## What are Skills?

Skills are markdown files that define custom commands you can invoke in Claude Code using slash commands (e.g., `/skill-name`). They allow you to:

- Create project-specific workflows
- Automate repetitive tasks
- Encapsulate domain knowledge
- Build custom development tools

## How to Use Skills

1. **Create a skill file**: Add a `.md` file to this directory
2. **Invoke the skill**: Use `/skill-name` in Claude Code (without the `.md` extension)
3. **Pass arguments**: Provide additional context or parameters after the skill name

Example:
```
/calculate-mortgage --price 300000 --down 20
```

## Skill File Format

Skills are markdown files with YAML frontmatter. Here's the basic structure:

```markdown
---
name: skill-name
description: Brief description of what this skill does
---

# Skill Instructions

Detailed instructions for Claude Code on how to execute this skill.

## Parameters

- `param1`: Description of parameter
- `param2`: Description of parameter

## Workflow

1. Step one
2. Step two
3. Step three

## Example Usage

Show examples of how to use this skill.
```

## Example Skills for This Project

Potential skills you could create:

- **calculate-mortgage**: Calculate mortgage payments with Tuscaloosa County taxes
- **update-tax-rates**: Update millage rates from current county data
- **validate-calculator**: Run validation tests on the calculator logic
- **deploy**: Deploy the calculator to a hosting service
- **optimize-html**: Optimize and minify the HTML file

## Getting Started

Check out the example skill file in this directory to see a working example specific to this project.

## Resources

- [Claude Code Skills Documentation](https://docs.anthropic.com/claude-code/skills)
- [Skill Examples Repository](https://github.com/anthropics/claude-code-examples)

## Contributing

When creating new skills:
- Use descriptive names (kebab-case)
- Include clear documentation
- Test skills before committing
- Update this README with new skill descriptions
