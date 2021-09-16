lunch: edison

edison:
	scrapy crawl edison
	open edison.ics

clean:
	rm -f edison.ics
