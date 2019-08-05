import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler

# readonly/train.csv - the training set (all tickets issued 2004-2011)
# readonly/test.csv - the test set (all tickets issued 2012-2016)
# readonly/addresses.csv & readonly/latlons.csv - mapping from ticket id to addresses, and from addresses to lat/lon coordinates. 

train = pd.read_csv('readonly/train.csv', encoding = 'ISO-8859-1')
test = pd.read_csv('readonly/test.csv')
address = pd.read_csv('readonly/addresses.csv')
latlons = pd.read_csv('readonly/latlons.csv')
train = train[ (train['compliance']  == 1) | (train['compliance']  == 0)]

address = address.set_index('address').join(latlons.set_index('address'), how = 'left')

train = train.set_index('ticket_id').join(address.set_index('ticket_id'))
test = test.set_index('ticket_id').join(address.set_index('ticket_id'))
train = train[~train['hearing_date'].isnull()]
drop1  = ['balance_due', 'collection_status', 'compliance_detail', 'payment_amount', 'payment_date', 'payment_status' ]
drop_string = ['violator_name', 'zip_code', 'country', 'city',
            'inspector_name', 'violation_street_number', 'violation_street_name',
            'violation_zip_code', 'violation_description',
            'mailing_address_str_number', 'mailing_address_str_name',
            'non_us_str_code', 'agency_name', 'state', 'disposition',
            'ticket_issued_date', 'hearing_date', 'grafitti_status', 'violation_code']
train.drop(drop1,axis = 1, inplace = True)
train.drop(drop_string, axis =1, inplace = True)
test.drop(drop_string, axis = 1, inplace = True)
train.lat.fillna(method='pad', inplace=True)
train.lon.fillna(method='pad', inplace=True)
test.lat.fillna(method='pad', inplace=True)
test.lon.fillna(method='pad', inplace=True)

y_train = train.compliance
X_train = train.drop('compliance', axis =1 )
X_test = test

scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# clf = MLPClassifier(hidden_layer_sizes = [100, 10], alpha = 0.001, random_state = 0, solver='lbfgs').fit(X_train_scaled, y_train)
clf = RandomForestClassifier(n_estimators = 10, random_state = 0).fit(X_train_scaled,y_train)
y_test = clf.predict_proba(X_test_scaled)[:,1]
test2 = pd.read_csv('readonly/test.csv')
test2['compliance'] = y_test
test2.set_index('ticket_id', inplace = True)

result = test2.compliance

def blight_model():

    return 
result