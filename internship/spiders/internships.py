from sys import intern
import scrapy

from internship.items import InternshipItem


class InternshipsSpider(scrapy.Spider):
    name = "internships"
    allowed_domains = ["github.com"]
    start_urls = ["https://github.com/SimplifyJobs/Summer2025-Internships"]

    def parse(self, response):
        for internship in response.css("#repo-content-pjax-container > div > div > div > div.Layout-main > react-partial > div > div > div.Box-sc-g0xbh4-0.vIPPs > div.Box-sc-g0xbh4-0.csrIcr > div > div.Box-sc-g0xbh4-0.QkQOb.js-snippet-clipboard-copy-unpositioned > article > markdown-accessiblity-table > table > tbody > tr"):
            item = InternshipItem()

            item["url"] = internship.css("td:nth-child(4) > a::attr(href)").get()
            if not item["url"]:
                continue
            
            item["company"] = internship.css("td:nth-child(1) > strong > a::attr(href)").get()
            if not item["company"]:
                item["company"] = internship.css("td:nth-child(1)::text").get()

            item["title"] = internship.css("td:nth-child(2)::text").get()
            item["date"] = internship.css("td:nth-child(5)::text").get()
            
            item["location"] = internship.css("td:nth-child(3)::text").get()
            if not item["location"]:
                item["location"] = ', '.join(internship.css("td:nth-child(3) > details *::text").getall())
            yield item
