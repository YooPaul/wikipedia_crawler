# wikipedia_crawler

Create a directory called "dict" and "images"

```mkdir dict```
~~~mkdir images~~~

Run ```python wiki_crawler.py page_keyword``` replacing page_keyword with the name of a wikipedia page you want to search for.
This will download metadata related to that page and store it inside the "dict" directory.

Now run ```python downloader.py page_keyword1 [page_keyword2 page_keyword3 ...]``` to download images associated with
each wikipedia page keyword provided as arguments. This will remove duplicate images from different pages. Results will be downloaded under the "images" folder.
