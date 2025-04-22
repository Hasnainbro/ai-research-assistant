from tavily import TavilyClient
TAVILY_API_KEY = "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"

client = TavilyClient(api_key=TAVILY_API_KEY)

def research_agent(query: str) -> str:
    results = client.search(query=query, max_results=5)

    combined_content = ""
    for result in results["results"]:
        combined_content += f"\nSource: {result['url']}\n{result['content']}\n"

    return combined_content.strip()
