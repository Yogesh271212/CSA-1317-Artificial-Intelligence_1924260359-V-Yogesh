def train_decision_tree(data, labels):
  approved_incomes = [
      row[1] for row, label in zip(data, labels) if label == 'Approved'
  ]
  approved_scores = [
      row[2] for row, label in zip(data, labels) if label == 'Approved'
  ]
  return min(approved_incomes), min(approved_scores)


def predict_loan(applicant, income_threshold, score_threshold):
  age, income, credit_score = applicant
  if income >= income_threshold and credit_score >= score_threshold:
    return 'Approved'
  return 'Rejected'


X = [
    [25, 30000, 600],
    [35, 60000, 750],
    [45, 80000, 800],
    [20, 15000, 500],
    [30, 40000, 650],
    [50, 90000, 780],
]
y = ['Rejected', 'Approved', 'Approved', 'Rejected', 'Rejected', 'Approved']

inc_thresh, score_thresh = train_decision_tree(X, y)
new_applicant = [32, 60000, 750]
prediction = predict_loan(new_applicant, inc_thresh, score_thresh)

print('Applicant Details (Age, Income, CreditScore):', new_applicant)
print('Loan Status Prediction:', prediction)
