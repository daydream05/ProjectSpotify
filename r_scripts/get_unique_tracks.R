#Set working directory as the directory of your project file


data <- read_csv("top200/top200_combined/top200_daily.csv")
data <- data %>% filter(!is.na(URL))
unique_songs <- data %>% select(`Track Name`, Artist, URL) %>% 
  unique()

write_csv(unique_songs, "top200/top200_combined/unique_tracks.csv")
