import scrapy
from ..items import CelebritiesItem

class CelebritiySpider(scrapy.Spider):

    domain_set = {'https://www.forbesindia.com/celebprofile2019/virat-kohli/1819/1'}

    name = 'celebrities'
    start_urls = [
        'https://www.forbesindia.com/celebprofile2019/virat-kohli/1819/1'
    ]

    def parse(self, response):
        items = CelebritiesItem()


        image_url = response.css('div.image-wrap img::attr(src)').extract()
        Name = response.css('h1::text').extract()
        profession = [response.css('tr:nth-child(1) td+ td::text')[0].extract().strip()]
        source_of_income = [response.css('tr:nth-child(2) td+ td::text')[0].extract().strip()]
        career_high_point = [response.css('tr:nth-child(3) td+ td::text')[0].extract().strip()]
        number_of_times_on_forbes_list_since_2017 = [response.css('tr:nth-child(4) td+ td::text')[0].extract().strip()]
        earnings_2019 = [response.css('tr:nth-child(5) td+ td::text')[0].extract().strip()]
        profile = response.css('.consumption-desc p::text').extract()

        items['image_url'] = image_url
        items['Name'] = Name
        items['profession'] = profession
        items['source_of_income'] = source_of_income
        items['career_high_point'] = career_high_point
        items['number_of_times_on_forbes_list_since_2017'] = number_of_times_on_forbes_list_since_2017
        items['earnings_2019'] = earnings_2019
        items['profile'] = profile

        yield items

        next_page = response.css('.celeb-grid:nth-child(1) div.view-profile a::attr(href)')[0].extract()

        if next_page not in CelebritiySpider.domain_set:
            CelebritiySpider.domain_set.add(next_page)
            yield response.follow(next_page, callback=self.parse)
