# Simulated Search Tool - replace with ADK Search tool integration
import time

class SearchTool:
    def __init__(self):
        pass

    async def search(self, query, limit=5):
        # Simulated search results (placeholder)
        time.sleep(0.1)
        results = [
            {
                "title": "Radar Handbook - Blind Speeds (Simulated)",
                "url": "https://example.com/radar/blind-speeds",
                "snippet": "Derivation of blind speeds and Doppler ambiguities."
            },
            {
                "title": "MTI Radar Delay-line Canceller",
                "url": "https://example.com/mti/canceller",
                "snippet": "Basics of delay-line cancellers in MTI radar."
            }
        ]
        return results[:limit]
