import pandas as pd
x = {
    'day':[1,2,3,4,5],
    'visitors':[100,200,300,400,500],
    'rate':[2,4,5,3,2]
}
y =pd.DataFrame(x)
#print(y)
#print(y.head(2))
print(y.tail(2))

#  merging 
import pandas as pd
x1 =pd.DataFrame({"index":[2001,2002,2003,2004],
    "hpi":[80,85,88,85],
    "rate":[2,3,2,2],
    "usp":[50,55,65,55]
}) 
x2 = pd.DataFrame({"index":[2005,2006,2007,2008],
    "hpi":[80,85,88,85],
    "rate":[2,3,2,2],
    "usp":[50,55,65,55]
})

m = pd.merge(x1,x2,on = "hpi")
print(m)

# joinings 
import pandas as pd
x1 = pd.DataFrame({"hpi":[2,3,4,5,6],"rating":[2,3,4,1,2]}, index = [2000,2001,2002,2003,2004])
x2 = pd.DataFrame({"low_price":[5000,6000,7000,8000,9000],"high_price":[10000,11000,12000,13000,14000]},index = [2000,2002,2003,2004,2005])
j =x1.join(x2)
print(j)

#  changing the column name 
import pandas as pd
x1 =pd.DataFrame({"index":[2001,2002,2003,2004],
    "hpi":[80,85,88,85],
    "rate":[2,3,2,2],
    "usp":[50,55,65,55]})
x2 = x1.rename(columns = {"rate":"rating"})
print(x2)
# change the index position
import pandas as pd
x1 =pd.DataFrame({"year":[2001,2002,2003,2004],
    "hpi":[80,85,88,85],
    "rate":[2,3,2,2],
    "usp":[50,55,65,55]})
#print(x1)
x2 = x1.set_index("rate")
print(x2)

# concatenation 
import pandas as pd
x1 =pd.DataFrame({
    "score":[90,91,92,93,94,95],
    "grade":[1,2,3,4,5,6],
    "rating":[1,2,3,4,5,6]},index = [2000,2001,2002,2003,2004,2009]
)
x2 = pd.DataFrame({
    "score":[99,97,96,95],
    "grade":[7,8,9,10],
    "rating":[7,8,9,10]},index = [2005,2006,2007,2008])
print(x1)
print(x2)
x = pd.concat([x1,x2])
print(x)

# single dimensional 
import pandas as pd
data = [1,2,3,4,5]
series = pd.Series(data)
print(series)

# changing index in single dimensional by using pandas library 
import pandas as pd
data = [1,2,3,4,5]
series = pd.Series(data)
series = pd.Series(data,index = ["a","b","c","d","e"])
print(series)
