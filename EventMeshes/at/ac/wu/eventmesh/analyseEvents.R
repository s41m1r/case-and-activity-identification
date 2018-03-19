library(dplyr)
library(reshape2)

filename <- "/home/saimir/git/nm-event-relations/Code/EventMeshes/at/ac/wu/eventmesh/allEvents.csv"
allEvents <- read.csv2(filename, sep = ',', header = TRUE)

id <- allEvents$hits__id
index <- allEvents$hits__index
score <- allEvents$hits__score
version <- allEvents$hits__source_.version
timestamp <- allEvents$hits__source_.timestamp
cacheKey <- allEvents$hits__source_cacheKey
cacheState <- allEvents$hits__source_cacheState
host <- allEvents$hits__source_host
iDirection <- allEvents$hits__source_inDirection
inHttpCode <- allEvents$hits__source_inHttpCode
inHttpHeaders <- allEvents$hits__source_inHttpHeaders
inHttpType <- allEvents$hits__source_inHttpType
inInterface <- allEvents$hits__source_inInterface
inMethodName <- allEvents$hits__source_inMethodName
logjClass <- allEvents$hits__source_logjClass
logjHost <- allEvents$hits__source_logjHost
logjLevel <- allEvents$hits__source_logjLevel
logjTimestamp <- allEvents$hits__source_logjTimestamp
magmaTransactionId <- allEvents$hits__source_magmaTransactionId
message <- allEvents$hits__source_message
outDirection <- allEvents$hits__source_outDirection
outEndpoint <- allEvents$hits__source_outEndpoint
outHttpCode <- allEvents$hits__source_outHttpCode
outHttpHeaders <- allEvents$hits__source_outHttpHeaders
outHttpType <- allEvents$hits__source_outHttpType
outInterface <- allEvents$hits__source_outInterface
outMethodName <- allEvents$hits__source_outMethodName
outReqId <- allEvents$hits__source_outReqId
payload <- allEvents$hits__source_payload
tags0 <- allEvents$hits__source_tags_0
tags1 <- allEvents$hits__source_tags_1
transactionId <- allEvents$hits__source_transactionId
sourceType <- allEvents$hits__source_type
hitstype <- allEvents$hits__type
hitsTimestamp <- allEvents$hits_fields_.timestamp_
highlight_inHttpHeaders <- allEvents$hits_highlight_inHttpHeaders_
highlight_magmaTransactionId <- allEvents$hits_highlight_magmaTransactionId_
highlight_message <- allEvents$hits_highlight_message_
highlight_outHttpHeaders <- allEvents$hits_highlight_outHttpHeaders_
highlight_payload <- allEvents$hits_highlight_payload_
sort <- allEvents$hits_sort_

allEventsMatrix <- as.matrix(allEvents)

class(allEventsMatrix)
attributes(allEventsMatrix)
sapply(allEventsMatrix[1,], class)

smallPortion <- head(allEventsMatrix, 50)

t <- table(smallPortion)
head(t)
inMethodName <- table(inMethodName)
head(inMethodName)
distinct(head(allEvents))

crs <- head(cars, 5)
table(t)

### Elaboration of the data

cor <- cor(smallPortion)
