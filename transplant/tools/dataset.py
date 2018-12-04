import pandas as pd
import numpy as np
import warnings
import datetime
from sklearn.model_selection import train_test_split

from transplant.config import PATH_STATIC_CLEAN, PATH_DYNAMIC_CLEAN, STATIC_CATEGORIES


class Dataset:
    """
    Transform csv patient and donors into a dimension dataset that
    can be used for modeling. Following steps are applied:
    Step 1 - Select a subset of columns
    Step 2 - Build the target variable
    Step 3 - Export data
    """

    test = False
    train = False
    time_offset = 30

    _random_state = 1

    def __init__(self, test=False, train=False, time_offset=30):
        self.test = test
        self.train = train
        self.time_offset = time_offset

    def get_static(self):

        data = pd.read_csv(PATH_STATIC_CLEAN)

        data = data[STATIC_CATEGORIES['patient_preoperative'] +
                    STATIC_CATEGORIES['donor_filtered'] +
                    STATIC_CATEGORIES['patient_postoperative_filtered']]

        # See https://github.com/dataforgoodfr/batch_5_transplant/blob/master/data/README.md#target

        data['target'] = np.nan

        # Success A
        data['target'] = np.where((data.immediate_extubation == 1) &
                                  (data.secondary_intubation == 0), 1, np.nan)

        # Success B
        data['target'] = np.where((data.target == 1) |
                                  ((data.immediate_extubation == 0) &
                                  (data.secondary_intubation == 0) &
                                  (data.LOS_first_ventilation < 2) &
                                  (data.Survival_days_27_10_2018 >= 2)), 1, 0)

        # Drop post_operation variables
        data.drop(['secondary_intubation',
                   'immediate_extubation',
                   'LOS_first_ventilation',
                   'Survival_days_27_10_2018'],
                  inplace=True,
                  axis=1)

        return self._sample_data(data)

    def get_dynamic(self):

        df = pd.read_csv(PATH_DYNAMIC_CLEAN)

        df['time'] = pd.to_datetime(df.time)

        # Truncate dynamic file to time_offset before end of operation

        tmp_offset = df[['id_patient', 'time']].groupby('id_patient') \
                                               .agg(['max']) \
                                               .reset_index()
        tmp_offset.columns = tmp_offset.columns.droplevel(1)
        tmp_offset['offset_time'] = \
            tmp_offset.time - datetime.timedelta(minutes=self.time_offset)

        df = pd.merge(df, tmp_offset[['id_patient', 'offset_time']],
                      on='id_patient')
        df = df[df['time'] < df['offset_time']]
        df.drop(['offset_time'], inplace=True, axis=1)

        # Filter result based on static set

        selector = self.get_static()['id_patient']
        df = df[df.id_patient.isin(selector)]

        return df

    def _sample_data(self, df):
        if not self.test and not self.train:
            return df

        train_df, test_df = train_test_split(df,
                                             test_size=0.3,
                                             random_state=self._random_state)

        if self.train:
            return train_df

        if self.test:
            return self._drop_target_column(test_df)

    def _drop_target_column(self, df):
        return df.drop(['target'], axis=1)
