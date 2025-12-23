#!/usr/bin/env python3
"""
API Bridge Module
Provides communication layer between Echo core and Cognitive Crystal AI backend.
"""

import asyncio
import logging
from typing import Dict, Any, Optional, Callable
import aiohttp
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class BridgeConfig:
    """Configuration for API Bridge"""
    backend_url: str = "http://localhost:5000"
    timeout: int = 30
    retry_attempts: int = 3
    retry_delay: float = 1.0


class APIBridge:
    """
    API Bridge for connecting Echo system components to Cognitive Crystal AI backend.
    
    This bridge handles:
    - Sensory input forwarding (audio, text, emotion)
    - Command reception from backend
    - Bidirectional communication between components
    """
    
    def __init__(self, config: Optional[BridgeConfig] = None):
        self.config = config or BridgeConfig()
        self.session: Optional[aiohttp.ClientSession] = None
        self.callbacks: Dict[str, Callable] = {}
        
    async def __aenter__(self):
        """Async context manager entry"""
        await self.connect()
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit"""
        await self.disconnect()
        
    async def connect(self):
        """Establish connection to backend"""
        if self.session is None:
            self.session = aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(total=self.config.timeout)
            )
            logger.info(f"API Bridge connected to {self.config.backend_url}")
            
    async def disconnect(self):
        """Close connection to backend"""
        if self.session:
            await self.session.close()
            self.session = None
            logger.info("API Bridge disconnected")
    
    def register_callback(self, event_type: str, callback: Callable):
        """Register a callback for specific event types"""
        self.callbacks[event_type] = callback
        logger.debug(f"Registered callback for event: {event_type}")
        
    async def send_sensory_input(self, input_type: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Send sensory input to backend.
        
        Args:
            input_type: Type of sensory input ('audio', 'text', 'emotion')
            data: Sensory data to send
            
        Returns:
            Response from backend
        """
        if not self.session:
            raise RuntimeError("API Bridge not connected")
            
        endpoint = f"{self.config.backend_url}/api/sensory/{input_type}"
        
        for attempt in range(self.config.retry_attempts):
            try:
                async with self.session.post(endpoint, json=data) as response:
                    response.raise_for_status()
                    try:
                        result = await response.json()
                        logger.debug(f"Sent {input_type} input to backend: {result}")
                        return result
                    except (aiohttp.ContentTypeError, ValueError) as e:
                        logger.error(f"Invalid JSON response for {input_type}: {e}")
                        return {"error": "invalid_json", "message": str(e)}
            except aiohttp.ClientError as e:
                logger.warning(f"Attempt {attempt + 1} failed for {input_type}: {e}")
                if attempt < self.config.retry_attempts - 1:
                    await asyncio.sleep(self.config.retry_delay)
                else:
                    raise
                    
        return {}
    
    async def send_text(self, text: str, metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Send transcribed text to backend"""
        data = {"text": text, "metadata": metadata or {}}
        return await self.send_sensory_input("text", data)
        
    async def send_emotion(self, arousal: float, valence: float, 
                          metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Send emotional state to backend"""
        data = {
            "arousal": arousal,
            "valence": valence,
            "metadata": metadata or {}
        }
        return await self.send_sensory_input("emotion", data)
        
    async def send_audio_features(self, features: Dict[str, Any]) -> Dict[str, Any]:
        """Send audio features to backend"""
        return await self.send_sensory_input("audio", features)
        
    async def get_command(self) -> Optional[Dict[str, Any]]:
        """
        Poll for commands from backend.
        
        Returns:
            Command dict if available, None otherwise
        """
        if not self.session:
            raise RuntimeError("API Bridge not connected")
            
        endpoint = f"{self.config.backend_url}/api/commands/poll"
        
        try:
            async with self.session.get(endpoint) as response:
                if response.status == 200:
                    try:
                        command = await response.json()
                        await self._process_command(command)
                        return command
                    except (aiohttp.ContentTypeError, ValueError) as e:
                        logger.error(f"Invalid JSON in command response: {e}")
                        return None
                elif response.status == 204:
                    # No commands available
                    return None
                else:
                    response.raise_for_status()
        except aiohttp.ClientError as e:
            logger.error(f"Error polling for commands: {e}")
            
        return None
        
    async def _process_command(self, command: Dict[str, Any]):
        """Process received command by calling registered callbacks"""
        command_type = command.get("type")
        if command_type and command_type in self.callbacks:
            callback = self.callbacks[command_type]
            try:
                if asyncio.iscoroutinefunction(callback):
                    await callback(command)
                else:
                    callback(command)
            except Exception as e:
                logger.error(f"Error processing command {command_type}: {e}")
                
    async def send_status(self, status: Dict[str, Any]) -> Dict[str, Any]:
        """Send system status to backend"""
        if not self.session:
            raise RuntimeError("API Bridge not connected")
            
        endpoint = f"{self.config.backend_url}/api/status"
        
        try:
            async with self.session.post(endpoint, json=status) as response:
                response.raise_for_status()
                try:
                    return await response.json()
                except (aiohttp.ContentTypeError, ValueError) as e:
                    logger.error(f"Invalid JSON response from backend: {e}")
                    return {"error": "invalid_json", "message": str(e)}
        except aiohttp.ClientError as e:
            logger.error(f"Error sending status: {e}")
            return {}


async def main():
    """Example usage of API Bridge"""
    logging.basicConfig(level=logging.INFO)
    
    config = BridgeConfig(backend_url="http://localhost:5000")
    
    async with APIBridge(config) as bridge:
        # Example: Send text input
        response = await bridge.send_text("Hello from Echo system")
        print(f"Backend response: {response}")
        
        # Example: Send emotion
        response = await bridge.send_emotion(arousal=0.7, valence=0.5)
        print(f"Emotion response: {response}")
        
        # Example: Poll for commands
        command = await bridge.get_command()
        if command:
            print(f"Received command: {command}")


if __name__ == "__main__":
    asyncio.run(main())
