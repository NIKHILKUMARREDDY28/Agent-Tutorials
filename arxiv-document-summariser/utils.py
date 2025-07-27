import arxiv


def search_arxiv(search_query: str, max_results: int = 5):
    """
    Search for papers on arXiv based on a search query.

    Args:
        search_query (str): The query to search for.
        max_results (int): The maximum number of results to return.

    Returns:
        list: A list of dictionaries containing paper metadata.
    """

    arxiv_client = arxiv.Client()

    search_results = arxiv.Search(
        query=search_query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance,
    )

    results = []
    for result in arxiv_client.results(search_results):
        results.append({
            "title": result.title,
            "authors": [author.name for author in result.authors],
            "summary": result.summary,
            "published": result.published.isoformat(),
            "arxiv_url": result.entry_id,
        })

    return results

if __name__ == '__main__':
    # Example usage
    query = "machine learning"
    papers = search_arxiv(query, max_results=3)
    for paper in papers:
        print(f"Title: {paper['title']}")
        print(f"Authors: {', '.join(paper['authors'])}")
        print(f"Published: {paper['published']}")
        print(f"Summary: {paper['summary']}\n")
        print(f"arXiv URL: {paper['arxiv_url']}\n")
        print("-" * 80)