# grepapp-scraper

A Python script to search and scrape code repositories from [grep.app](https://grep.app/) using customizable search queries and filters.

## Features

- Search code repositories based on keywords, language, and page range.
- Filter repositories based on a specified language (supports multiple languages).
- Optionally exclude results based on keywords.
- Save repository URLs to a file.
- Optionally view code snippets with the `--show-snippet` argument.
- Support for regular expressions in search queries.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/grepapp-scraper.git
   cd grepapp-scraper

2. Install dependencies:

```
pip install -r requirements.txt
```


## Usage
You can use this script from the command line as follows:

```
python grepapp_scraper.py --search-term "<search-term>" --lang "<language>" --max <number-of-pages> [--show-snippet] [--exclude "<comma-separated-exclude-terms>"]
```

## Arguments:
* --search-term <term>: Search term to match in the code repositories (required).
* --lang <language>: Comma-separated list of languages to filter results by (e.g., Python,JavaScript) (required).
* --max <number>: Maximum number of pages to scrape. Default is 4.
* --show-snippet: Option to display the code snippet for each search result.
* --exclude <terms>: Option to exclude results containing specified terms (comma-separated).


## Example Usage

Search for repositories containing the term encryption in both Python and JavaScript code:

```
python grepapp_scraper.py --search-term "encryption" --lang "Python,JavaScript" --max 3
```


Search with the term encryption, exclude results containing test, and show code snippets:

```
python grepapp_scraper.py --search-term "encryption" --lang "Python,JavaScript" --max 3 --show-snippet --exclude "test"
```

If you want to both display results and save them to a CSV:
```
python3 run.py --search-term "encryption" --lang "Python,JavaScript" --max 3 --csv

```



##  Output

By default, the script will print the repository URLs found in the search. If --show-snippet is enabled, it will also display a code snippet from the results.

Repositories are also saved to a file (repositories.txt) if the `--get-only-repos` flag is set.