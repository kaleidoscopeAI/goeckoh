# Setup and Configuration Guide

## Complete Echo-Crystal AGI System Setup

This guide provides step-by-step instructions for setting up and configuring the integrated Echo-Crystal AGI system after integrating files from the echovoice project.

## Prerequisites

### System Requirements
- **Operating System**: Linux (Ubuntu/Debian recommended), macOS, or Windows
- **Python**: 3.8 or later
- **Node.js**: 14.x or later (for frontend)
- **RAM**: Minimum 8GB, 16GB+ recommended
- **Storage**: 5GB free space minimum

### Required System Packages

#### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install -y \
    python3-dev \
    python3-pip \
    portaudio19-dev \
    ffmpeg \
    build-essential
```

#### macOS
```bash
brew install portaudio ffmpeg
```

#### Windows
- Install Python from python.org
- Install Visual C++ Build Tools
- Install ffmpeg and add to PATH

## Installation Steps

### Step 1: Clone or Update Repository

```bash
# If not already cloned
git clone https://github.com/kaleidoscopeAI/goeckoh.git
cd goeckoh

# If already cloned, pull latest changes
git pull origin main
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/macOS:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 3: Install Python Dependencies

```bash
# Install complete dependencies
pip install --upgrade pip
pip install -r requirements_complete.txt

# Or install minimal dependencies
pip install -r requirements.txt
```

### Step 4: Install Node.js Dependencies (for frontend)

```bash
# If frontend exists
npm install
```

### Step 5: Configure the System

#### Copy and Edit Configuration Files

```bash
# Copy example configuration
cp config.yaml config.local.yaml

# Edit configuration
nano config.local.yaml  # or use your preferred editor
```

#### Configuration File Structure

The `config.yaml` file should contain:

```yaml
# Backend Configuration
backend:
  url: "http://localhost:5000"
  timeout: 30
  
# Echo Core Configuration
echo:
  audio_device: null  # null for default device
  sample_rate: 16000
  model: "base"  # Whisper model: tiny, base, small, medium, large
  
# ABA Engine Configuration
aba:
  enabled: true
  strategies:
    - calming
    - engagement
    - redirection
  threshold:
    arousal: 0.7
    valence: 0.3
    
# Organic AI Configuration
organic:
  enabled: true
  node_limit: 1000
  mutation_rate: 0.01
  
# Voice Synthesis Configuration
voice:
  tts_model: "tts_models/en/ljspeech/tacotron2-DDC"
  voice_profile_path: null  # Path to reference voice WAV file
  
# LLM Configuration
llm:
  provider: "ollama"
  model: "llama2"
  base_url: "http://localhost:11434"
  
# Logging Configuration
logging:
  level: "INFO"
  file: "logs/system.log"
```

### Step 6: Copy Additional Files from EchoVoice Project

If you have files from the echovoice project, copy them as needed:

```bash
# Copy icon
cp /home/jacob/Desktop/echovoice/icon.png icons/icon.png

# Copy any additional integration scripts
# (Only if they don't already exist in goeckoh)
```

## Running the System

### Option 1: Using the Unified Launcher (Recommended)

```bash
./run_all.sh
```

Or with custom configuration:

```bash
./run_all.sh config.local.yaml INFO
```

### Option 2: Using Python Script

```bash
python3 run_unified.py --config config.yaml --log-level INFO
```

### Option 3: Running Components Separately

#### Start Backend (if applicable)
```bash
cd cognitive-nebula
python3 backend/main.py
```

#### Start Frontend (if applicable)
```bash
cd frontend
npm run dev
```

#### Start Echo Core
```bash
python3 echo_core.py
```

## Testing

### Run Integration Tests

```bash
python3 test_integration.py
```

### Run System Tests

```bash
python3 test_system.py
```

## Verification

### Check System Status

```bash
# Check if backend is running
curl http://localhost:5000/api/status

# Check Python environment
python3 -c "import yaml, aiohttp, numpy; print('Dependencies OK')"

# Check audio devices
python3 -c "import sounddevice; print(sounddevice.query_devices())"
```

## Troubleshooting

### Common Issues

#### Issue: ModuleNotFoundError
**Solution**: Ensure virtual environment is activated and dependencies are installed:
```bash
source venv/bin/activate
pip install -r requirements_complete.txt
```

#### Issue: Audio device not found
**Solution**: List available audio devices and update config:
```bash
python3 -c "import sounddevice; print(sounddevice.query_devices())"
```

#### Issue: Backend connection failed
**Solution**: Ensure backend is running on correct port:
```bash
# Check if port 5000 is in use
netstat -tuln | grep 5000
```

#### Issue: Permission denied on run_all.sh
**Solution**: Make script executable:
```bash
chmod +x run_all.sh
```

## Configuration Wiring Details

### Component Communication

The system integrates multiple components:

1. **Echo Core** (`echo_core.py`)
   - Processes audio input
   - Generates emotional metrics
   - Runs ABA evaluation
   
2. **API Bridge** (`api_bridge.py`)
   - Connects Echo to backend
   - Handles bidirectional communication
   - Manages command routing
   
3. **Cognitive Crystal AI Backend**
   - Crystalline memory
   - Thought engines
   - Organic AI
   - LLM integration
   
4. **Frontend**
   - Visualization
   - User interaction
   - Real-time monitoring

### Data Flow

```
[Microphone] → [Echo Core] → [API Bridge] → [Backend]
                                               ↓
                                          [Crystalline Memory]
                                               ↓
                                          [Thought Engines]
                                               ↓
                                          [Decision Making]
                                               ↓
[Speaker] ← [Voice Synthesis] ← [API Bridge] ← [Commands]
```

## Next Steps

1. Review the ECHOVOICE_INTEGRATION.md document for detailed integration information
2. Check integration_wiring_diagram.md for architectural details
3. Run integration tests to verify setup
4. Customize configuration for your specific use case
5. Add any missing files from echovoice project as needed

## Support

For issues or questions:
1. Check existing documentation in `docs/` directory
2. Review integration guides
3. Check system logs in `logs/` directory
4. Consult TROUBLESHOOTING section above

## Security Notes

- Never commit sensitive credentials to the repository
- Use environment variables for API keys and secrets
- Keep `config.local.yaml` in .gitignore
- Regularly update dependencies for security patches
