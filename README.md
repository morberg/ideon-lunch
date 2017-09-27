# Create a calendar file with this week's menu

List available crawlers with `scrapy list`. Select the restaurant you want an .ics file for, e.g. `edison`.

Run the crawler with:

`scrapy crawl edison`

to create `edison.ics` which will this week's menu as daily calendar entries 11:30-12:00. 

Open the file with your preferred application:

`open Ideon Edison.ics`

Enjoy!

## Create a new restaurant crawler

Creating a new spider:

`scrapy genspider <name> <domain>`

Test your expression to extract info with `scrapy shell`. This might require some trial and error if the HTML is not well formed. It seldom is.

Modify the file `lunch/spiders/<name>.py`:

1. Add `restaurant` variable to class
2. Modify the `start_urls` variable
2. Implement the `parse` method to yield `weekday` and `courses` for each day of the week