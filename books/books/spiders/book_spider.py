import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    file= open("books.txt","a",encoding="UTF-8")
    book_count=1
    page_count=0
    start_urls = ["https://www.kitapyurdu.com/index.php?route=product/category/&filter_category_all=true&category_id=1&sort=purchased_365&order=DESC&filter_in_stock=1",
            
        ]
    def parse(self, response):
        book_names=response.css("div.name.ellipsis a span::text").getall()
        book_authors=response.css("div.author span a span::text").getall()
        book_publishers=response.css("div.publisher span a span::text").getall()

        i=0
        while(i < len(book_names)):

            #(if you want to create json, use it this.)
            """yield {
                "name": book_names[i],
                "author": book_authors[i],
                "publishers": book_publishers[i],
            }"""
            self.file.write("-----------------------\n")
            self.file.write(str(self.book_count)+"\n")
            self.file.write("Book Name:" + book_names[i]+"\n")
            self.file.write("Author:" + book_authors[i]+"\n")
            self.file.write("Publisher:"+book_publishers[i]+"\n")
            self.book_count +=1
            i +=1
        next_url=response.css("a.next::attr(href)").get()
        self.page_count +=1
        if next_url is not None :  #and self.page_count!=5#(if you want to write just 5 page, you can use it)
           
            yield scrapy.Request(url=next_url,callback=self.parse)
        else:
            self.file.close()



