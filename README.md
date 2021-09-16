# Create a calendar file with this week's menu
## Fast food

Run:

`make lunch`

This will run the crawler for Edison and then open the generated calendar file.

## Recipe

List available crawlers with `scrapy list`. Select the restaurant you want an .ics file for, e.g. `edison`.

Run the crawler with:

`scrapy crawl edison`

to create `edison.ics`. This week's daily courses will be calendar entries 11:30-12:00. 

Open the file with your preferred calendar application:

`open edison.ics`

# Create a JSON file
Scrapy has built in support for exporting to JSON. Simply run:

`scrapy crawl bricks -o bricks.json`

to create a JSON file with this week's menu for the `bricks` restaurant.

# Create a new restaurant crawler
First you need to figure out what data to extract. Navigate to the web page of the restaurant you want to create a spider for. Look at the source. Then run:

`scrapy shell http://my.local.restaurant.com`

and experiment to find the expression you need to extract the daily menu items.

Some example expressions currently used by `ideon-lunch` are:

* `response.xpath('//div[@id=$val]/table//td[@class="course_description"]/p/text()', val=day).extract()`
* `response.xpath('//div[@class="grid2column"][contains(text(), $val)]/following-sibling::div[@class="item-description-menu"]', val=day).xpath('normalize-space(.)').extract()`
* `response.xpath('//div[@class="lunch"]//h3[contains(text(), $val)]/following-sibling::table[1]/tr/td[2]', val=day).xpath('normalize-space(.)').extract()`

Once you have your expression you can create a new spider with:

`scrapy genspider <name> <domain>`

Modify the file `lunch/spiders/<name>.py`:

1. Add `restaurant` variable to class with the name of the restaurant
2. Modify the `start_urls` variable
2. Implement the `parse` method to yield `weekday` and `courses` for each day of the week

## Fixing a broken restaurant

```
scrapy shell http://restaurangedison.se/lunch
response.xpath('//div[@id=$val]/table//td[@class="course_description"]/p/text()', val='monday').extract()
```
and iterate.