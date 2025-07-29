import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/SAdrian/api/moviesdatabase'

mcp = FastMCP('moviesdatabase')

@mcp.tool()
def x_titles_by_ids(idsList: Annotated[str, Field(description="Imdb id's comma separated -> tt0001702,tt0001856,tt0001856 ...")],
                    list: Annotated[Union[str, None], Field(description='Selected list -> most_pop_movies / most_pop_series / top_rated_series_250 / ...')] = None,
                    info: Annotated[Union[str, None], Field(description='Info type structure (default: mini-info) -> base_info / mini_info / image / ...')] = None) -> dict: 
    '''Titles by ids list'''
    url = 'https://moviesdatabase.p.rapidapi.com/titles/x/titles-by-ids'
    headers = {'x-rapidapi-host': 'moviesdatabase.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'idsList': idsList,
        'list': list,
        'info': info,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_by_imdb_id(id: Annotated[str, Field(description='')]) -> dict: 
    '''Search by imdb id'''
    url = 'https://moviesdatabase.p.rapidapi.com/titles/tt0086250'
    headers = {'x-rapidapi-host': 'moviesdatabase.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def title_title(exact: Annotated[Union[bool, None], Field(description='Search by exact title')] = None,
                info: Annotated[Union[str, None], Field(description='Info type structure (default: mini-info) -> base_info / mini_info / image /...')] = None,
                year: Annotated[Union[int, float, None], Field(description='Year filter ex: ?year=2020')] = None,
                page: Annotated[Union[str, None], Field(description='Page number')] = None,
                sort: Annotated[Union[str, None], Field(description='Add sorting (incr, decr) -> year.incr /year.decr')] = None,
                endYear: Annotated[Union[int, float, None], Field(description='Year range filter -to- ex: ?endYear=2020')] = None,
                startYear: Annotated[Union[int, float, None], Field(description='Year range filter -from- ex: ?startYear=2020')] = None,
                titleType: Annotated[Union[str, None], Field(description='Filter by type of title')] = None,
                limit: Annotated[Union[int, float, None], Field(description='Number of titles per page (default: 10) -> 10 max')] = None,
                list: Annotated[Union[str, None], Field(description='Selected list -> most_pop_movies / most_pop_series / top_rated_series_250 / ...')] = None) -> dict: 
    '''Search by Title'''
    url = 'https://moviesdatabase.p.rapidapi.com/titles/search/title/%7Btitle%7D'
    headers = {'x-rapidapi-host': 'moviesdatabase.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'exact': exact,
        'info': info,
        'year': year,
        'page': page,
        'sort': sort,
        'endYear': endYear,
        'startYear': startYear,
        'titleType': titleType,
        'limit': limit,
        'list': list,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
