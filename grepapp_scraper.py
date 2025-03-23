import click
import requests

SEARCH_URL = 'https://grep.app/api/search?q={}&{}&page={}'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

def fetch_results(term, languages, exclude, max_pages, show_snippet):
    results = []
    page = 1

    lang_filters = "&".join([f"f.lang={lang}" for lang in languages.split(',')])

    while page == 1 or (results and (not max_pages or page <= max_pages)):
        page_url = SEARCH_URL.format(term, lang_filters, page)
        print(f"Fetching: {page_url}")
        response = requests.get(page_url, headers=HEADERS)

        try:
            result_page_json = response.json()
        except requests.exceptions.JSONDecodeError:
            click.echo("Error: Invalid JSON response")
            break

        hits = result_page_json.get('hits', {}).get('hits', [])
        if not hits:
            break  # Stop if no new results

        for hit in hits:
            repo = hit['repo']['raw']
            path = hit['path']['raw']
            snippet = hit['content']['snippet'] if show_snippet else None

            results.append({
                "repo": repo,
                "path": path,
                "snippet": snippet
            })

        click.echo(f'Got {len(hits)} results from page {page}')
        page += 1

    # Apply exclude filter if provided
    if exclude:
        exclude_words = set(exclude.split(','))
        results = [r for r in results if not any(word in r['repo'] for word in exclude_words)]

    return results

@click.command()
@click.option('--search-term', required=True, type=str, help='Search term to match')
@click.option('--lang', required=True, type=str, help='Filter results by language (comma-separated, e.g., Python,Java)')
@click.option('--exclude', default='', type=str, help='Exclude results by keywords (comma-separated)')
@click.option('--max', default=4, type=int, help='Maximum pages to fetch results from')
@click.option('--show-snippet', is_flag=True, help='Show code snippets in output')
def scrape(search_term, lang, exclude, max, show_snippet):
    results = fetch_results(search_term, lang, exclude, max, show_snippet)
    click.echo(f'Found {len(results)} results.')

    for res in results:
        click.echo(f"\nRepository: {res['repo']}")
        click.echo(f"File Path: {res['path']}")
        if show_snippet and res["snippet"]:
            click.echo("Code Snippet:")
            click.echo(res["snippet"])
        click.echo("-" * 40)

if __name__ == '__main__':
    scrape()
