
div_num = function(){
  num1 = as.numeric(readline("Enter the first number: "))
  num2 = as.numeric(readline("Enter the second number: "))
  print(num1/num2)
}
k=1
add_num = function(){
  num1 = as.numeric(readline("Enter the first number: "))
  num2 = as.numeric(readline("Enter the second number: "))
  print(num1+num2)
}

sub_num = function(){
  num1 = as.numeric(readline("Enter the first number: "))
  num2 = as.numeric(readline("Enter the second number: "))
  print(num1-num2)
}

mul_num = function(){
  num1 = as.numeric(readline("Enter the first number: "))
  num2 = as.numeric(readline("Enter the second number: "))
  print(num1*num2)
}
while(k){
  print("Menu of Arithmetic operators:")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. To Exit type 0")
  userChoice = as.integer(readline("User choice: "))
  print(userChoice)
  
  if(userChoice==1){
    add_num()
  }
 
  if(userChoice==2){
    sub_num()
  }

  if(userChoice==3){
    mul_num()
  }
}
  if(userChoice==4){
    div_num()
  }
  if(userChoice==5){
    k=0
  }
  
}

print("Exit sucessfully!")


