library(dplyr)
library(data.table)
library(iterators)
setwd("D:/fall 2016/data warehousing/projectspotify")

all_url <- fread("all_download_url.csv", data.table = FALSE)
country_names <- fread("spotipy_script/country_names.csv", data.table = FALSE)
country_names <- country_names %>% filter(code != 'mx')
all_url <- all_url %>% filter(code != 'mx')
dates <- seq(as.Date("2015/09/01"),
             as.Date("2016/09/01"),
             "days")

file_names <- as.character(dates)

for(code in country_names$code){
  dest_file = paste("country_list", code, sep='/')
  dir.create(dest_file)
  print(paste("Succesfully created", code, "directory"))
  
  for(link in all_url$url){
    print(paste("Downloading ", code, "...", sep=""))
    
    date = strsplit(link, "/")[[1]][7]
    
    destination = paste(dest_file, '/', date, "-", code, ".csv", sep='')
    download.file(link, destination)
    print(paste("Finished downloading", code, sep=" "))
  }
  
}


