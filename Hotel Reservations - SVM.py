import pandas as pd
from sklearn.svm import SVC
from imblearn.over_sampling import SVMSMOTE
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

data = pd.read_csv('Hotel_Reservations.csv', low_memory = False)
data.drop('Booking_ID', axis = 1, inplace = True)
half_count = len(data)
data = data.dropna(thresh = half_count,axis = 1)
data['room_type_reserved']  = pd.factorize(data['room_type_reserved'])[0].astype(int)
data['type_of_meal_plan']   = pd.factorize(data['type_of_meal_plan'])[0].astype(int)
data['market_segment_type'] = pd.factorize(data['market_segment_type'])[0].astype(int)
data['booking_status']      = pd.factorize(data['booking_status'])[0].astype(int)
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values
svm_estimator = SVC()
svmsmote = SVMSMOTE(k_neighbors = 5, svm_estimator = svm_estimator)
X_resampled, y_resampled = svmsmote.fit_resample(X, y)
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size = 0.3, random_state = 42)

svm_model = SVC(C = 10, gamma = 0.1)
svm_model.fit(X_train, y_train)
prediction = svm_model.predict(X_test)
print(classification_report(y_test, prediction))

