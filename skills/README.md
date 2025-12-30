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

## Available Skills

### Official Anthropic Skills

Downloaded from the [Anthropic Skills Repository](https://github.com/anthropics/skills):

**Creative & Design:**
- `/algorithmic-art` - Generate algorithmic art and visualizations
- `/canvas-design` - Design and create canvas-based graphics
- `/frontend-design` - Frontend web design assistance
- `/slack-gif-creator` - Create GIFs for Slack messages
- `/theme-factory` - Generate color themes and design systems

**Document Processing:**
- `/docx` - Create and manipulate Word documents
- `/pdf` - Comprehensive PDF manipulation toolkit
- `/pptx` - Create and edit PowerPoint presentations
- `/xlsx` - Work with Excel spreadsheets
- `/doc-coauthoring` - Collaborative document authoring

**Development & Technical:**
- `/mcp-builder` - Build Model Context Protocol servers
- `/skill-creator` - Create new Claude Code skills
- `/webapp-testing` - Test web applications
- `/web-artifacts-builder` - Build web artifacts and components

**Enterprise & Communication:**
- `/brand-guidelines` - Maintain brand consistency
- `/internal-comms` - Internal communications assistance

### Project-Specific Skills

Custom skills for this Tuscaloosa Mortgage Calculator project:

- `/update-tax-rates` - Update Tuscaloosa County property tax millage rates

### Ideas for Additional Custom Skills

Potential skills you could create:

- **calculate-mortgage**: Calculate mortgage payments with Tuscaloosa County taxes
- **validate-calculator**: Run validation tests on the calculator logic
- **deploy**: Deploy the calculator to a hosting service
- **optimize-html**: Optimize and minify the HTML file

## Getting Started

Check out the existing skill files in this directory to see working examples. The official Anthropic skills show advanced patterns, while `update-tax-rates.md` shows a project-specific example.

## Resources

- [Official Anthropic Skills Repository](https://github.com/anthropics/skills) - Source of all official skills
- [Claude Code Documentation](https://docs.anthropic.com/claude-code)
- [Awesome Claude Skills](https://github.com/travisvn/awesome-claude-skills) - Community curated list

## Contributing

When creating new skills:
- Use descriptive names (kebab-case)
- Include clear documentation
- Test skills before committing
- Update this README with new skill descriptions
