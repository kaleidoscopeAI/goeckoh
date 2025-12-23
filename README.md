# Goeckoh - Assistive Platform Monorepo

Welcome to the **Goeckoh** assistive platform monorepo! This repository consolidates multiple packages and services that work together to provide a comprehensive assistive technology solution.

## Monorepo Structure

This repository uses npm/yarn workspaces to manage multiple related packages:

```
packages/
├── voice/              # Voice client (echovoice) - to be imported
├── mobile-client/      # Mobile application
├── web-dashboard/      # Web-based dashboard
├── backend/            # Backend services and APIs
└── shared-models/      # Shared models and utilities
```

## Quick Start

### Prerequisites
- Node.js 18+ (for workspace management and web components)
- Python 3.8+ (for Python-based services)
- npm or yarn

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/kaleidoscopeAI/goeckoh.git
   cd goeckoh
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Set up individual packages:**
   Each package may have its own setup instructions. Refer to the README in each package directory.

## Merge Plan and Integration

### Phase 1: Scaffold Setup (Current)
- ✅ Create monorepo structure with workspace configuration
- ✅ Add placeholder directories for all packages
- ✅ Set up CI/CD workflow for the monorepo

### Phase 2: Import EchoVoice
**Next Steps:** Import the local echovoice codebase into `packages/voice/`

To import echovoice:

1. **Copy the local echovoice directory:**
   ```bash
   cp -r /home/jacob/Desktop/echovoice/* packages/voice/
   ```

2. **Review and commit:**
   ```bash
   git add packages/voice/
   git commit -m "Import echovoice codebase"
   git push origin add-echovoice-scaffold
   ```

3. **Open a follow-up PR** for integration testing and documentation updates.

See `packages/voice/README.md` for detailed import instructions.

### Phase 3: Integration and Testing
- Integrate echovoice with backend services
- Create mobile client interfaces
- Build web dashboard for monitoring and control
- Establish shared models and utilities
- Comprehensive integration testing

### Phase 4: Production Deployment
- Deploy backend services
- Release mobile applications
- Deploy web dashboard
- Set up monitoring and analytics

## Development

### Working with Workspaces

Run commands in a specific package:
```bash
npm run <script> -w packages/<package-name>
```

Run commands in all packages:
```bash
npm run <script> --workspaces
```

### Available Scripts

Check `package.json` in the root and each package for available scripts.

## Legacy Components

This repository also contains legacy Python-based components that will be gradually migrated or integrated:

- Python AI-Agent scaffold with REPL
- Voice cloning with Coqui TTS
- Configuration validation tools

See legacy documentation sections below for details on these components.

---

## Legacy Documentation

### Python AI-Agent (Legacy)

Minimal Python AI-Agent scaffold for validating a system config and starting a simple REPL agent.

Quick start:
1. python -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. python -m cli start

Commands:
- python -m cli validate  # validate config.yaml against config.schema.yaml
- python -m cli fix       # auto-fix common issues in config.yaml
- python -m cli start     # start a REPL with the agent

The default config.yaml includes guidance from the tools instructions.

Speak command (voice cloning required)
- This CLI enforces voice cloning. There is no fallback to local TTS.
- You MUST provide a clean WAV sample of your voice either via:
  - The config (voice_profile_path), or
  - The CLI (--voice-profile)
- The sample must be at least the minimum duration (default: 5 seconds) and sampled at 16kHz where possible.
- Example:
  - Record 5s and use recorded sample for cloning:
    python -m cli speak --record --duration 5 --voice-profile ./sample_voice.wav
  - Use an existing WAV sample and an input file to correct and play:
    python -m cli speak --input-file ./input.wav --voice-profile ./sample_voice.wav

Read documents
- Read all .txt/.md/.pdf files from a folder and its subfolders:
  python -m cli read-docs --path ./documents --recursive
- The command defaults to recursive reading. Use --no-recursive to restrict to the top-level folder only.
- Make sure the documents_path in config.yaml points to your folder if you don't pass --path.
- Subfolder contents are ingested and summarized automatically.

Read code
- Read all .py files from a folder and its subfolders:
  python -m cli read-code --path ./project --recursive
- The command defaults to recursive reading. Use --no-recursive to restrict to the top-level folder only.
- The command uses the same config.documents_path as a fallback if --path is not provided.

Notes:
- Voice cloning uses Coqui TTS and resemblyzer. The following packages are required — they are large and may require a GPU for fast synthesis:
  - TTS (Coqui TTS)
  - resemblyzer
- If the voice profile is missing, or the libraries cannot be initialized, the CLI will exit with an error.
- For accurate cloning, provide a clean voice sample (>= 5s) sampled at 16kHz WAV format.
