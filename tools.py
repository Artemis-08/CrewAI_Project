import os
from dotenv import load_dotenv

# Load environment before importing crewai_tools
load_dotenv()

# Try to import and create tool
try:
    from crewai_tools import YoutubeChannelSearchTool
    yt_tool = YoutubeChannelSearchTool(youtube_channel_handle='@krishnaik06')
except Exception as e:
    # If tool fails to initialize (ChromaDB issues), create a mock
    print(f"Warning: Failed to initialize YoutubeChannelSearchTool: {e}")
    print("Creating a mock tool for now...")
    
    from crewai.tools import BaseTool
    
    class MockYoutubeTool(BaseTool):
        name: str = "youtube_search"
        description: str = "Mock YouTube channel search tool - searches for content on @krishnaik06"
        
        def _run(self, query: str) -> str:
            return f"Mock search result for: {query} on @krishnaik06 channel"
    
    yt_tool = MockYoutubeTool()
