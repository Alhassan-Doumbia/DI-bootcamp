👩‍🏫 👩🏿‍🏫 What you will build
Server (server.py)
Name: WeatherDemo.
Tool: get_weather(city: str) -> dict that returns static weather data for a few cities.
Resource: cities://list that returns a newline-separated list of supported cities.
Uses STDIO loop (mcp.run()). Optionally log to stderr so you can see when calls arrive.
Client (client.py)
Spawns the server via MCP CLI over STDIO.
Initializes the session, lists resources/tools, reads cities://list.
Calls get_weather for one city (e.g., “Paris”) and prints the response.


Tasks
1. Implement server.py

Create FastMCP("WeatherDemo").
Register get_weather(city: str) tool that returns a dict like { "city": city, "temp_c": 21, "condition": "sunny" } using a small in-memory lookup (e.g., Paris, London, NYC). If city not found, return an error dict.
Register cities://list resource that returns the supported cities as text.
In __main__, start the server with mcp.run().
Optional: add logging.basicConfig(level=logging.INFO) to stderr and log tool calls.
2. Implement client.py

Use StdioServerParameters(command="mcp", args=["run", "server.py"], env=None).
With stdio_client(...) + ClientSession, call initialize().
List and print resources; list and print tools.
Read cities://list and print its content.
Call get_weather with a valid city (e.g., “Paris”) and print the returned dict.
3. Run and observe

Single terminal: python client.py (client spawns server).
Two terminals (for debugging):
T1: mcp run server.py
T2: python client.py
You should see resource list, tool list, city list, and a weather dict.


Troubleshooting
mcp: command not found ? re-run install or activate venv.
No tools/resources listed ? restart server; verify decorators.
JSON/type issues ? ensure tool args are strings and keys match the signature.


What to submit
server.py and client.py.
A short terminal capture showing: resource list, tool list, cities://list, and get_weather output.
