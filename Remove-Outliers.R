ReadData <- read.csv(file.choose()) # missing.csv
colSums(is.na(ReadData))
nrow(ReadData)
df<-ReadData
z <- df[df$AGE > quantile(df$AGE, .25) - 1.5*IQR(df$AGE) & 
          df$AGE < quantile(df$AGE, .75) + 1.5*IQR(df$AGE), ] #rows

nrow(z)




z <- z[z$GENDER > quantile(z$GENDER, .25) - 1.5*IQR(z$GENDER) & 
         z$GENDER < quantile(z$GENDER, .75) + 1.5*IQR(z$GENDER), ] #rows
nrow(z)


z <- z[z$HEIGHT > quantile(z$HEIGHT, .25) - 1.5*IQR(z$HEIGHT) & 
         z$HEIGHT < quantile(z$HEIGHT, .75) + 1.5*IQR(z$HEIGHT), ] #rows

nrow(z)

z <- z[z$WEIGHT > quantile(z$WEIGHT, .25) - 1.5*IQR(z$WEIGHT) & 
         z$WEIGHT < quantile(z$WEIGHT, .75) + 1.5*IQR(z$WEIGHT), ] #rows


nrow(z)

z <- z[z$AP_HIGH > quantile(z$AP_HIGH, .25) - 1.5*IQR(z$AP_HIGH) & 
         z$AP_HIGH < quantile(z$AP_HIGH, .75) + 1.5*IQR(z$AP_HIGH), ] #rows

nrow(z)

z <- z[z$AP_LOW > quantile(z$AP_LOW, .25) - 1.5*IQR(z$AP_LOW) & 
         z$AP_LOW < quantile(z$AP_LOW, .75) + 1.5*IQR(z$AP_LOW), ] #rows

nrow(z)


#z <- z[z$CHOLESTEROL > quantile(z$CHOLESTEROL, .25) - 1.5*IQR(z$CHOLESTEROL) & 
 #        z$CHOLESTEROL < quantile(z$CHOLESTEROL, .75) + 1.5*IQR(z$CHOLESTEROL), ] #rows

#nrow(z)

#z <- z[z$GLUCOSE > quantile(z$GLUCOSE, .25) - 1.5*IQR(z$GLUCOSE) & 
#         z$GLUCOSE < quantile(z$GLUCOSE, .75) + 1.5*IQR(z$GLUCOSE), ] #rows

#nrow(z)


#z <- z[z$SMOKE > quantile(z$SMOKE, .25) - 1.5*IQR(z$SMOKE) & 
#         z$SMOKE < quantile(z$SMOKE, .75) + 1.5*IQR(z$SMOKE), ] #rows

#nrow(z)


#z <- z[z$ALCOHOL > quantile(z$ALCOHOL, .25) - 1.5*IQR(z$ALCOHOL) & 
#         z$ALCOHOL < quantile(z$ALCOHOL, .75) + 1.5*IQR(z$ALCOHOL), ] #rows

#nrow(z)

#z <- z[z$PHYSICAL_ACTIVITY > quantile(z$PHYSICAL_ACTIVITY, .25) - 1.5*IQR(z$PHYSICAL_ACTIVITY) & 
#         z$PHYSICAL_ACTIVITY < quantile(z$PHYSICAL_ACTIVITY, .75) + 1.5*IQR(z$PHYSICAL_ACTIVITY), ] #rows

#nrow(z)

#z <- z[z$CARDIO_DISEASE > quantile(z$CARDIO_DISEASE, .25) - 1.5*IQR(z$CARDIO_DISEASE) & 
#         z$CARDIO_DISEASE < quantile(z$CARDIO_DISEASE, .75) + 1.5*IQR(z$CARDIO_DISEASE), ] #rows


#nrow(z)

write.csv(z,"C:\\Users\\Himanshu Patel\\Downloads\\cardiovascular-disease-dataset\\Cleansed_MyData.csv", row.names = TRUE)


