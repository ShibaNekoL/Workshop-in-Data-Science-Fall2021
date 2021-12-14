data <- read.csv(file.choose())

colnames(data)[1] <- c("seek_help")

datacut <- data[1:188,1:4]


datacut$seek_help <- ifelse(datacut$seek_help==1, "S","")
datacut$time <- ifelse(datacut$time==1, "T","")
datacut$material <- ifelse(datacut$material==1, "M","")
datacut$experience <- ifelse(datacut$experience==1, "E","")

datacut <- datacut[,1:4]
datacut$set <- paste0(datacut$seek_help, datacut$time, datacut$material, datacut$experience)

table(datacut$set)

