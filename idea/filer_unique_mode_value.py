# အဲ့ထဲမှာ user က 500 ပဲပါတာ..
# row က 80K+ ရှိတယ်.. ကျတော်က အဲ့ထဲကနေ user id နဲ့
# အယောက် 500 စာအတွက် row 500 ကိုပဲ သူတိုဝယ်တဲ့
# number of product, toal product per order, order day, order hour, day since order order
# နဲ့ဆွဲထုတ်ချင်တာ

import pandas as pd
wanted_columns = ['user_id',  'order_day_of_wk',
                   'order_hr_of_day', 'days_since_prior_order',
                   'add_to_cart_order', 'reordered',
                   'tot_prod_bought',
                   'tot_prod_per_order']


# read csv file
instacart_df = pd.read_csv('idea/instacart_dataset_final.csv')
selected_instacart_df = instacart_df[wanted_columns]

# group by with user_id
instacart_mode_only_df = selected_instacart_df.groupby(['user_id']).agg(lambda x:x.value_counts().index[0])
instacart_mode_only_df.reset_index(inplace=True)
instacart_mode_only_df.to_csv('idea/filered_instacart_mode.csv',index=False)