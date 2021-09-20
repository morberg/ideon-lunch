lunch: edison

edison:
	. .venv/bin/activate && scrapy crawl edison
	open edison.ics

clean:
	rm -f edison.ics
