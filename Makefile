lunch: edison

edison:
	. .venv/bin/activate && scrapy crawl edison
	open edison.ics

bricks:
	. .venv/bin/activate && scrapy crawl bricks

clean:
	rm -f *.ics *.json
