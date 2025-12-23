# Goeckoh - Assistive Platform Monorepo

This repository is being restructured as a monorepo to support multiple integrated packages for the assistive platform, including voice client, mobile client, web dashboard, backend services, and shared models.

## Repository Structure

```
goeckoh/
├── packages/
│   ├── voice/              # Voice client (echovoice to be imported)
│   ├── mobile-client/      # Mobile application
│   ├── web-dashboard/      # Web-based dashboard
│   ├── backend/            # Backend services
│   └── shared-models/      # Shared data models and utilities
├── .github/
│   └── workflows/          # CI/CD workflows
└── [existing root files]   # Legacy Python CLI and system files
```

## Monorepo Integration Plan

This PR scaffolds the monorepo structure and prepares for integrating the echovoice package.

### Next Steps: Importing Echovoice

**IMPORTANT:** The `packages/voice` directory is a placeholder. To import the local echovoice code:

1. **Copy the local echovoice folder into packages/voice:**
   ```bash
   # From the repository root
   cp -r /home/jacob/Desktop/echovoice/* packages/voice/
   ```

2. **Verify the import:**
   ```bash
   ls -la packages/voice/
   ```

3. **Stage and commit the changes:**
   ```bash
   git add packages/voice/
   git commit -m "feat: Import echovoice package"
   ```

4. **Push and create a follow-up PR:**
   ```bash
   git push origin <your-branch-name>
   # Then create a PR for review
   ```

See `packages/voice/README.md` for detailed instructions.

## Workspace Setup

This monorepo uses npm/yarn workspaces for package management:

```bash
# Install all dependencies across packages
npm install

# Run scripts from root
npm run <script-name>
```

## Legacy Python CLI

The root directory still contains the original Python AI-Agent scaffold. For legacy CLI usage:

Quick start:
1. python -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. python -m cli start

Commands:
- python -m cli validate  # validate config.yaml against config.schema.yaml
- python -m cli fix       # auto-fix common issues in config.yaml
- python -m cli start     # start a REPL with the agent

## Contributing

Please create feature branches for new work and submit PRs for review. Each package may have its own build and test scripts - see individual package READMEs.

## License

MIT License - see LICENSE file for details.
