import scrapy


class SongSpider(scrapy.Spider):
    name = "song"
    custom_settings ={
        'CLOSESPIDER_PAGECOUNT': 4

    }
    start_urls = [
        'http://www.npr.org/programs/morning-edition/',
    ]

    def parse(self, response):
        for show_link in response.css('div.episode-core-wrap'):
            yield {
                'episode_date': show_link.css('time::attr(datetime)').extract_first()
            }

        for show_link in response.css('div.song-meta-wrap'):
            yield {
                'song': show_link.css('span.song-meta-title::text').extract_first(),
                'artist': show_link.css('span.song-meta-artist::text').extract_first(),

            }

        next_page = response.css('li.prev a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

