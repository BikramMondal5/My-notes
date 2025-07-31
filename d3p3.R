 find_max = function(vector){
      max_val = vector[1]
      for(num in vector){
        if (num > max_val){
          max_val = num
          
        }
          
      }
      return (max_val)   
 }    
find_min = function(vector){
  min_val = vector[1]
  for(num in vector){
    if(num < min_val){
      min_val = num
      
    }
     
  }
  return (min_val) 
}
          
    
calculate_sum = function(vector){
  total = 0
  for(num in vector){
    total = total+num
    
    
  }
  return (total)  
}
    
calculate_mean = function(vector)
{
  len=0
  for(num in vector){
    len = len+1
  }
  total = calculate_sum(vector)
  mean = total/len
  new_mean = as.numeric(mean)
  return (new_mean)
}
  
    
main = function()
{
  vector = c(3L,5L,7L)
     
    
  max_val = find_max(vector)
  min_val = find_min(vector)
  total = calculate_sum(vector)
  mean = calculate_mean(vector)
      
  print(max_val)
  print(min_val)
  print(total)
  print(mean)
  
}
    
main()
    