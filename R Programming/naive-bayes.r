train=data.frame(
  age=c('youth','youth','mid-aged','senior','senior','senior','mid-aged','youth','youth','senior','youth','mid-aged','mid-aged','senior'),
  income=c('high','high','high','medium','low','low','low','medium','low','medium','medium','medium','high','medium'),
  student=c('no','no','no','no','yes','yes','yes','no','yes','yes','yes','no','yes','no'),
  credit_rating=c('fair','excellent','fair','fair','fair','excellent','excellent','fair','fair','fair','excellent','excellent','fair','excellent'),
  buys_comp=c('no','no','yes','no','no','yes','yes','no','yes','no','yes','yes','yes','yes')
)
prior_yes= sum(train$buys_comp == "yes") / nrow(train)
prior_no = sum(train$buys_comp == "no") / nrow(train)

cond_prob = function(feature, value, label) {
  subset = train[train$buys_comp == label, ]
  return(sum(subset[[feature]] == value) / nrow(subset))
}
# function using Naive Bayes
predict_nb = function(age, income, student, credit_rating) {
  
  p_yes = prior_yes
  p_no = prior_no
  
  p_age_yes = cond_prob("age", age, "yes")
  p_income_yes = cond_prob("income", income, "yes")
  p_student_yes= cond_prob("student", student, "yes")
  p_credit_yes= cond_prob("credit_rating", credit_rating, "yes")
  p_age_no = cond_prob("age", age, "no")
  p_income_no= cond_prob("income", income, "no")
  p_student_no = cond_prob("student", student, "no")
  p_credit_no = cond_prob("credit_rating", credit_rating, "no")
  prob_yes = p_yes * p_age_yes * p_income_yes * p_student_yes * p_credit_yes
  prob_no = p_no * p_age_no * p_income_no * p_student_no * p_credit_no
  
  # Normalize korchi
  total = prob_yes + prob_no
  prob_yes_norm = prob_yes / total
  prob_no_norm = prob_no / total
  prediction = ifelse(prob_yes_norm > prob_no_norm, "yes", "no")
  
  return (list(prediction = prediction, prob_yes = prob_yes_norm, prob_no = prob_no_norm))
  }
  
predict_nb("senior", "low", "no", "fair")
 
