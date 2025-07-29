# MoviesDatabase MCP Server

## Overview

The MoviesDatabase MCP server is a comprehensive platform for accessing extensive information on movies, TV shows, and actors. With a database encompassing over 9 million titles and 11 million actors, crew, and cast members, this server is designed to provide developers with up-to-date and detailed data, including YouTube trailer URLs, awards, full biographies, and many other useful details.

## Key Features

- **Vast Collection**: Access data for over 9 million titles and 11 million individuals involved in film and television.
- **Regular Updates**: Recent titles are updated weekly, while ratings and episode details are updated daily.
- **Detailed Information**: Obtain a wealth of information, from basic details to extensive data such as awards, ratings, and cast biographies.

## Tools and Endpoints

The MoviesDatabase MCP server provides several key tools and endpoints, allowing users to query and retrieve data efficiently:

### Titles
- **Titles - Multiple**: Retrieve an array of titles based on various filters and sorting parameters.
- **Titles by List of Id's**: Fetch titles using a list of specific IMDb IDs.
- **Title Details**: Access detailed information for a specific title using its IMDb ID.
- **Title Rating**: Get the rating and number of votes for a specific title.
- **Seasons and Episodes**: Retrieve episodes for a series, sorted by season and episode numbers.
- **Seasons Number**: Find out the total number of seasons for a series.
- **Episodes by Series and Season**: Get episodes for a specific series and season.
- **Upcoming Titles**: Discover upcoming titles with various filtering options.

### Search
- **Titles by Keyword**: Search for titles using specific keywords.
- **Titles by Title**: Search for titles using a full or partial title.
- **Titles by Aka's**: Find titles by alternative names, with exact matching.

### Actors
- **Actors**: Retrieve a list of actors based on filters.
- **Actor Details**: Access detailed information for a specific actor using their IMDb ID.

### Utils
- **Title Type**: List available title types.
- **Genres**: List available genres.
- **Titles Lists**: Access predefined lists of titles.

## Usage

Each endpoint returns an object with a 'results' key, and those with pages include additional keys such as 'page', 'next', and 'entries'. Query parameters are mostly optional, allowing for flexible data retrieval.

### Description of Optional Query Parameters

- **info**: Customize the data structure to receive.
- **limit**: Set the number of objects per page.
- **page**: Specify the page number for paginated results.
- **titleType**: Filter titles by type.
- **startYear** / **endYear**: Filter titles by a range of years.
- **year**: Filter titles by release year.
- **genre**: Filter titles by genre.
- **sort**: Sort results by predefined options.
- **exact**: Specify exact match for title searches.
- **list**: Choose from predefined lists of titles.

## Conclusion

The MoviesDatabase MCP server is an invaluable resource for developers seeking comprehensive and up-to-date information on movies, TV shows, and actors. With its wide array of tools and endpoints, it offers flexibility and depth in data retrieval and management, supporting a broad range of use cases in the entertainment industry.