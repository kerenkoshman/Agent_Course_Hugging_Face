"""
Basic Weather Agent Demo
=======================

A simple agent that demonstrates agent architecture using smolagents and Ollama.
This version simulates weather data for demonstration purposes.
"""

import random
from smolagents import LiteLLMModel
from typing import Dict, Any

class WeatherAgent:
    def __init__(self):
        """Initialize the weather agent with LLM."""
        # Initialize the LLM (using your working Ollama setup)
        self.llm = LiteLLMModel(
            model_id="ollama/qwen2:7b",
            api_base="http://127.0.0.1:11434",
            num_ctx=8192,
        )
        
        # Simulated weather data for demonstration
        self.weather_data = {
            "New York": {"temp": 22, "condition": "sunny", "humidity": 65},
            "London": {"temp": 15, "condition": "cloudy", "humidity": 80},
            "Tokyo": {"temp": 28, "condition": "partly cloudy", "humidity": 70},
            "Paris": {"temp": 18, "condition": "rainy", "humidity": 85},
            "Sydney": {"temp": 25, "condition": "clear", "humidity": 60},
            "Toronto": {"temp": 12, "condition": "windy", "humidity": 75},
            "Berlin": {"temp": 16, "condition": "overcast", "humidity": 78},
            "Moscow": {"temp": 8, "condition": "cold", "humidity": 82}
        }
    
    def get_weather(self, city: str) -> Dict[str, Any]:
        """
        Get simulated current weather for a city.
        
        Args:
            city: City name
            
        Returns:
            Dictionary with weather information
        """
        if city in self.weather_data:
            data = self.weather_data[city]
            return {
                "city": city,
                "temperature": f"{data['temp']}°C",
                "condition": data["condition"],
                "humidity": f"{data['humidity']}%",
                "wind_speed": f"{random.randint(5, 25)} km/h"
            }
        else:
            # Generate random weather for unknown cities
            return {
                "city": city,
                "temperature": f"{random.randint(10, 30)}°C",
                "condition": random.choice(["sunny", "cloudy", "rainy", "clear"]),
                "humidity": f"{random.randint(50, 90)}%",
                "wind_speed": f"{random.randint(5, 25)} km/h"
            }
    
    def get_weather_forecast(self, city: str) -> Dict[str, Any]:
        """
        Get simulated 5-day weather forecast for a city.
        
        Args:
            city: City name
            
        Returns:
            Dictionary with forecast information
        """
        conditions = ["sunny", "cloudy", "rainy", "clear", "partly cloudy", "overcast"]
        forecast = []
        
        for i in range(5):
            forecast.append({
                "date": f"Day {i+1}",
                "temperature": f"{random.randint(10, 30)}°C",
                "condition": random.choice(conditions)
            })
        
        return {
            "city": city,
            "forecast": forecast
        }
    
    def process_query(self, user_query: str) -> str:
        """
        Process a user query and return a response.
        
        Args:
            user_query: User's weather-related question
            
        Returns:
            Agent's response
        """
        # Simple logic to determine if we need weather data
        if any(word in user_query.lower() for word in ["weather", "temperature", "forecast"]):
            # Extract city name (simple approach)
            cities = list(self.weather_data.keys()) + ["San Francisco", "Los Angeles", "Chicago", "Miami"]
            city = None
            for c in cities:
                if c.lower() in user_query.lower():
                    city = c
                    break
            
            if not city:
                city = "New York"  # Default city
            
            # Get weather data
            if "forecast" in user_query.lower():
                weather_data = self.get_weather_forecast(city)
                response_text = f"Here's the 5-day forecast for {weather_data['city']}:\n\n"
                for day in weather_data['forecast']:
                    response_text += f"📅 {day['date']}: {day['temperature']}, {day['condition']}\n"
            else:
                weather_data = self.get_weather(city)
                response_text = f"Current weather in {weather_data['city']}:\n"
                response_text += f"🌡️ Temperature: {weather_data['temperature']}\n"
                response_text += f"🌤️ Condition: {weather_data['condition']}\n"
                response_text += f"💨 Wind Speed: {weather_data['wind_speed']}\n"
                response_text += f"💧 Humidity: {weather_data['humidity']}\n"
            
            return response_text
        else:
            # For non-weather queries, use the LLM
            try:
                response = self.llm.client.completion(
                    model="ollama/qwen2:7b",
                    messages=[{"role": "user", "content": user_query}],
                    max_tokens=100,
                    temperature=0.7
                )
                return response.choices[0].message.content
            except Exception as e:
                return f"Sorry, I encountered an error: {str(e)}"

def main():
    """Main function to test the weather agent."""
    print("🌤️  WEATHER AGENT DEMO")
    print("=" * 50)
    print("This agent demonstrates basic agent architecture with simulated weather data.")
    print("In a real implementation, you would connect to a weather API.\n")
    
    # Initialize the agent
    agent = WeatherAgent()
    
    # Test queries
    test_queries = [
        "What's the weather like in New York?",
        "Tell me the forecast for London",
        "How's the weather in Tokyo?",
        "What's the temperature in Paris?",
        "Hello! How are you?",
        "What's the weather in San Francisco?",
        "Give me the forecast for Los Angeles"
    ]
    
    for query in test_queries:
        print(f"\n🤔 User: {query}")
        print(f"🤖 Agent: {agent.process_query(query)}")
        print("-" * 50)

if __name__ == "__main__":
    main()
