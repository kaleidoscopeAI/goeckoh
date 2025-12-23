#!/bin/bash
# Run All Components - Unified System Launcher
# This script launches the complete Echo-Crystal AGI system

set -e  # Exit on error

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Echo-Crystal AGI System Launcher${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ] && [ ! -d "new_venv" ]; then
    echo -e "${YELLOW}No virtual environment found. Creating one...${NC}"
    python3 -m venv venv
    echo -e "${GREEN}Virtual environment created.${NC}"
fi

# Activate virtual environment
if [ -d "venv" ]; then
    echo -e "${GREEN}Activating virtual environment (venv)...${NC}"
    source venv/bin/activate
elif [ -d "new_venv" ]; then
    echo -e "${GREEN}Activating virtual environment (new_venv)...${NC}"
    source new_venv/bin/activate
fi

# Check if dependencies are installed
if ! python -c "import yaml" 2>/dev/null; then
    echo -e "${YELLOW}Installing dependencies...${NC}"
    if [ -f "requirements.txt" ]; then
        pip install -r requirements.txt
    fi
fi

# Configuration
CONFIG_FILE="${1:-config.yaml}"
LOG_LEVEL="${2:-INFO}"

# Check if config file exists
if [ ! -f "$CONFIG_FILE" ]; then
    echo -e "${YELLOW}Configuration file $CONFIG_FILE not found.${NC}"
    echo -e "${YELLOW}Using default configuration.${NC}"
fi

echo ""
echo -e "${GREEN}Configuration:${NC}"
echo -e "  Config file: $CONFIG_FILE"
echo -e "  Log level: $LOG_LEVEL"
echo ""

# Function to cleanup on exit
cleanup() {
    echo ""
    echo -e "${YELLOW}Shutting down system...${NC}"
    # Kill any background processes
    jobs -p | xargs -r kill 2>/dev/null || true
    echo -e "${GREEN}Shutdown complete.${NC}"
}

trap cleanup EXIT INT TERM

# Launch the system
echo -e "${GREEN}Starting unified system...${NC}"
echo ""

python3 run_unified.py \
    --config "$CONFIG_FILE" \
    --log-level "$LOG_LEVEL"

exit_code=$?

if [ $exit_code -eq 0 ]; then
    echo -e "${GREEN}System exited successfully.${NC}"
else
    echo -e "${RED}System exited with error code: $exit_code${NC}"
fi

exit $exit_code
