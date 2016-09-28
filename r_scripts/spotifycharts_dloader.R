library(dplyr)
library(readr)
dates <- seq(as.Date("2015/09/01"),
             as.Date("2016/09/01"),
             "days")

file_names <- as.character(dates)
url <- "https://spotifycharts.com/regional/global/daily/"

download_charts <- function(file_names, url){
  for (i in seq(file_names)){
    url_path <- paste(url, file_names[i], "/download", sep="")
    dest_path <- paste(file_names[i], ".csv", sep="")
    download.file(url_path, dest_path)
  }
}

data <- read_csv(paste(file_names[1], ".csv", sep=""))


add_date_column <- function(table, date)
{
 table <- table %>% mutate(Date = as.Date(date)) 
 return(table)
}


first_table <- read_csv(paste(file_names[1], ".csv", sep=""))
first_table <- add_date_column(first_table, file_names[1])

load_files <- function(files, first_table){
  # initialize the first table so there is a table we can bind
  initial_table <-  first_table
  for(i in 2:length(files)){
    data <- read_csv(paste(files[i], ".csv", sep=""))
    data <- add_date_column(table = data,
                            date = as.Date(files[i]))
    initial_table <- bind_rows(initial_table, data)
  }
  return(initial_table)
  }

final <- load_files(file_names, first_table)

clean_final <- final %>%
  filter(!is.na(URL), is.na(`<!doctype html>`))

no_doc_column <- clean_final[,1:6]

complete_case <- complete.cases(no_doc_column)
length(complete_case)

has_doctype <- final %>% 
  filter(!is.na(`<!doctype html>`))

error_dates <- as.character(unique(has_doctype$Date))
#re-download dates that are empty.
download_charts(error_dates, url)

#THERE IS NO DATA ON 9-24-2015


final_clean <- load_files(error_dates, no_doc_column)
final_clean <- final_clean %>% filter(Date != '2015-09-24')
final_clean <- final_clean[,1:6]

#Add 09-01-2016 because I didn't add it initially. Remove these lines if you are running the script from the beginning.

by_dates <- final_clean %>% group_by(Date) %>%
  summarise(n = n())
ouput_csv <- write_csv(final_clean, "top200_daily.csv")

