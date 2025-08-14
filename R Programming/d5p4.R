# Load Iris dataset first, display the summary of the dataset.
dataset = iris

summary(dataset)

# i) Indentify the type of column
typeof(dataset$Sepal.Length)
typeof(dataset$Sepal.Width)
typeof(dataset$Petal.Length)
typeof(dataset$Petal.Width)
typeof(dataset$Species)

# ii) Display the first 20 rows of the dataset
head(dataset, 20)

# Find the correlation of each features column with the class column using the build-in function. Match the result with the result obtained by user defined function

cor(dataset$Sepal.Length,dataset$Sepal.Width)

# create a user defined function correlation function
correlation = function(x,y){
  X_mean = mean(x)
  y_mean = mean(y)
  n=length(x)
  sdx = sqrt(sum(x^2)/n-mean(x^2))
  sdy = sqrt(sum(x^2)/n-mean(y^2))
  numenitor = sum(x*y)-n*sdx*sdy
  denominator = n*sdx*sdy
  r=numenitor/denominator
  return (r)
}
x=dataset$Sepal.Length
y=dataset$Sepal.Width
correlation(x,y)
 
# Make a bar plot of the entries which show the frequency distribution of each class

species_counts = table(dataset$Species)
print(species_counts)

# Create bar plot
barplot(species_counts,main = "Frequency Distribution of Iris Species",xlab = "Species",ylab = "Count",col = c("lightblue", "lightgreen", "lightcoral"),border = "black")
