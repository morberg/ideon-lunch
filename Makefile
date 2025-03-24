lunch: edison

edison:
	uv run scrapy crawl edison
	open edison.ics

bricks:
	uv run scrapy crawl bricks

clean:
	rm -f *.ics *.json
