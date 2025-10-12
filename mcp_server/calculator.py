from typing import Any
from mcp.server.fastmcp import FastMCP


# Initialize FastMCP server
mcp = FastMCP("calculator", log_level="ERROR")


@mcp.tool()
def calculate_string(string: str) -> Any: 
# output type can be restricted to just int or float if only numeric results are expected
    """Calculate the operations for a given string using Python's eval function.

    Args:
        string: The input string to evaluate.
    """
    try:
        # Evaluate the string and return the result
        result = eval(string)
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}
    
    
if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')