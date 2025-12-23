#!/usr/bin/env python3
"""
Complete Integrated System
Integrates Echo voice processing with Cognitive Crystal AI backend.
"""

import asyncio
import logging
import signal
import sys
from pathlib import Path
from typing import Optional
import yaml

try:
    from api_bridge import APIBridge, BridgeConfig
except ImportError as e:
    print(f"Error: Cannot import api_bridge module: {e}")
    print("Please ensure api_bridge.py is present and dependencies are installed.")
    sys.exit(1)

logger = logging.getLogger(__name__)


class IntegratedSystem:
    """
    Complete integrated system combining:
    - Echo Core (speech processing, emotional analysis, ABA engine)
    - Cognitive Crystal AI (AGI backend, organic AI, crystalline memory)
    - API Bridge (communication layer)
    """
    
    def __init__(self, config_path: str = "config.yaml"):
        self.config_path = config_path
        self.config = self._load_config()
        self.bridge: Optional[APIBridge] = None
        self.running = False
        
        # Setup signal handlers for graceful shutdown
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)
        
    def _load_config(self) -> dict:
        """Load system configuration"""
        config_file = Path(self.config_path)
        if config_file.exists():
            with open(config_file, 'r') as f:
                config = yaml.safe_load(f)
                logger.info(f"Loaded configuration from {self.config_path}")
                return config
        else:
            logger.warning(f"Config file {self.config_path} not found, using defaults")
            return self._default_config()
            
    def _default_config(self) -> dict:
        """Default configuration"""
        return {
            "backend": {
                "url": "http://localhost:5000",
                "timeout": 30
            },
            "echo": {
                "audio_device": None,
                "sample_rate": 16000,
                "model": "base"
            },
            "aba": {
                "enabled": True,
                "strategies": ["calming", "engagement", "redirection"]
            },
            "organic": {
                "enabled": True,
                "node_limit": 1000
            }
        }
        
    def _signal_handler(self, signum, frame):
        """Handle shutdown signals"""
        logger.info(f"Received signal {signum}, shutting down...")
        self.running = False
        
    async def initialize(self):
        """Initialize all system components"""
        logger.info("Initializing integrated system...")
        
        # Initialize API Bridge
        bridge_config = BridgeConfig(
            backend_url=self.config.get("backend", {}).get("url", "http://localhost:5000"),
            timeout=self.config.get("backend", {}).get("timeout", 30)
        )
        self.bridge = APIBridge(bridge_config)
        await self.bridge.connect()
        
        # Register command callbacks
        self.bridge.register_callback("speech", self._handle_speech_command)
        self.bridge.register_callback("aba", self._handle_aba_command)
        self.bridge.register_callback("hid", self._handle_hid_command)
        
        logger.info("System initialization complete")
        
    async def shutdown(self):
        """Shutdown all system components"""
        logger.info("Shutting down integrated system...")
        
        if self.bridge:
            await self.bridge.disconnect()
            
        logger.info("System shutdown complete")
        
    async def _handle_speech_command(self, command: dict):
        """Handle speech generation command from backend"""
        text = command.get("text", "")
        prosody = command.get("prosody", {})
        logger.info(f"Speech command: {text} with prosody {prosody}")
        
        # TODO: Integrate with VoiceCrystal/Coqui TTS
        # For now, just acknowledge
        await self.bridge.send_status({
            "type": "speech_complete",
            "text": text
        })
        
    async def _handle_aba_command(self, command: dict):
        """Handle ABA strategy command from backend"""
        strategy = command.get("strategy", "")
        logger.info(f"ABA command: {strategy}")
        
        # TODO: Integrate with AbaEngine
        # For now, just acknowledge
        await self.bridge.send_status({
            "type": "aba_complete",
            "strategy": strategy
        })
        
    async def _handle_hid_command(self, command: dict):
        """Handle HID emulation command from backend"""
        action = command.get("action", "")
        logger.info(f"HID command: {action}")
        
        # TODO: Integrate with HID emulation
        # For now, just acknowledge
        await self.bridge.send_status({
            "type": "hid_complete",
            "action": action
        })
        
    async def process_audio_input(self, audio_data: bytes):
        """
        Process audio input from microphone.
        This would integrate with Echo Core's audio processing pipeline.
        """
        # TODO: Integrate actual audio processing
        # For now, just a placeholder
        logger.debug("Processing audio input")
        
    async def run(self):
        """Main run loop for integrated system"""
        await self.initialize()
        
        self.running = True
        logger.info("Integrated system running...")
        
        try:
            while self.running:
                # Main processing loop
                # Poll for commands from backend
                command = await self.bridge.get_command()
                
                # TODO: Process audio input
                # TODO: Update emotional state
                # TODO: Run ABA evaluation
                # TODO: Update organic AI
                
                # Small delay to prevent tight loop
                await asyncio.sleep(0.1)
                
        except Exception as e:
            logger.error(f"Error in main loop: {e}", exc_info=True)
        finally:
            await self.shutdown()


async def main():
    """Main entry point for integrated system"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    system = IntegratedSystem()
    await system.run()


if __name__ == "__main__":
    asyncio.run(main())
