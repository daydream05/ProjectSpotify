library(dplyr)

dates <- seq(as.Date("2015/09/01"),
             as.Date("2016/08/31"),
             "days")

file_names <- as.character(dates)
url <- "https://spotifycharts.com/regional/global/daily/"

for (i in seq(file_names)){
  url_path <- paste(url, file_names[i], "/download", sep="")
  dest_path <- paste(file_names[i], ".csv", sep="")
  download.file(url_path, dest_path)
}
