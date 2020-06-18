# install.packages("rvest")
library(rvest)
lego_movie <- html("http://www.imdb.com/title/tt1490017/")

lego_movie %>%
  html_node("#relatedEditorialListsWidget") %>%
  html_text()

regexpr("[0-9]{0,4}.[0-9]{0,4}", "alek $123.33")

replace(c("asdf"))


sub("alek", "bob", c("alekalekalek", "asdfasdfalek"))


price_web = html("https://www.mlbshop.com/boston-red-sox/kids/t-14224197+ga-14+z-920092-2887796110")
price_stuff2 <- price_web %>%
  html_nodes(".regular-price") %>%
  html_text()
sub(" \\$", "", sub("Regular: \\$", "", price_stuff2))
