import json
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import csv


# Function to convert a CSV to JSON
# Takes the file paths as arguments
def csvFile(request):
    # create a dictionary
    data = {}
    csvFilePath = 'script_json/static/csvFiles/coronavirus.csv'
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
            # Assuming a column named 'No' to
            # be the primary key
            key = rows['Sno']
            data[key] = rows
    print(data)
    json_data = json.dumps(data)
    # return HttpResponse(data,content_type='application/json')
    return JsonResponse(data)



def jsonData(request):
    script = '''
        import pandas as pd
        import numpy as np
        from numpy import sqrt, abs, round
        from scipy.stats import norm
        from scipy import stats as st

        batch = pd.read_csv('../BatchesAndSamples/BatchesAndSamples/APG_Covid19_Batch_till20201106.csv', index_col=False)

        columns = ['sender','batchID','Covid19Batch_id','receptionDateTime','clippingCompletionDateTime','swabType','puidCompleteClipping', 'machineName']
        batch_df = batch[columns]

        # Getting the batch prefix (1st two lettters)
        batch_df['batch_prefix'] = batch_df['batchID'].str.slice(0, 2)
        batch_df

        A3_A8_A93 = ['A3 Passau', 'A8 Traunstein', 'A93 Rosenheim']
        Flughafen = ['Flughafen München','Flughafen Memmingen','Flughafen Nürnberg']
        LKT = ['LKT BY Amberg-Sulzbach','LKT BY Bayreuth','LKT BY Berchtesgadener Land','LKT BY Dillingen','LKT BY Fürstenfeldbruck',
               'LKT BY Freising','LKT BY Freyung Grafenau','LKT BY Haar','LKT BY Kulmbach','LKT BY Miesbach','LKT BY Miltenberg',
               'LKT BY Neuburg-Schrobenhausen','LKT BY Passau','LKT BY Pfaffenhofen','LKT BY Regen','LKT BY Regensburg',
               'LKT BY Rosenheim','LKT BY Roth','LKT BY Rottal Inn','LKT BY Schweinfurt','LKT BY Straubing-Bogen','LKT BY Tirschenreuth',
               'LKT BY Traunstein','LKT BY Würzburg']

               # batch_df.sender[1]
        batch_df['Merged_sender'] = batch_df['sender']

        for i in range(len(batch_df)):
            if batch_df.sender[i] in A3_A8_A93:
                batch_df['Merged_sender'][i] = 'A3_A8_A93'
            elif batch_df.sender[i] in Flughafen:
                batch_df['Merged_sender'][i] = 'Flughafen'
            elif batch_df.sender[i] in LKT:
                batch_df['Merged_sender'][i] = 'LKT'
            else:
                batch_df['Merged_sender'][i] = batch_df.sender[i]

        batch_df

        sampleAug1_df = pd.read_csv('../BatchesAndSamples/BatchesAndSamples/Sample_20200801_20200810.csv')
        sampleAug2_df = pd.read_csv('../BatchesAndSamples/BatchesAndSamples/Sample_20200810_20200820.csv')
        sampleAug3_df = pd.read_csv('../BatchesAndSamples/BatchesAndSamples/Sample_20200820_20200831.csv')
        sampleSep1_df = pd.read_csv('../BatchesAndSamples/BatchesAndSamples/Sample_20200901_20200910.csv')
        sampleSep2_df = pd.read_csv('../BatchesAndSamples/BatchesAndSamples/Sample_20200910_20200920.csv')
        sampleSep3_df = pd.read_csv('../BatchesAndSamples/BatchesAndSamples/Sample_20200920_20200930.csv')
        sampleOct1_df = pd.read_csv('../BatchesAndSamples/BatchesAndSamples/Sample_20201001_20201007.csv')
        sampleOct2_df = pd.read_csv('../BatchesAndSamples/BatchesAndSamples/Sample_20201008_20201014.csv')
        sampleTillDate_df = pd.read_csv('../BatchesAndSamples/BatchesAndSamples/APG_Covid19_Sample_from20201015_till20201106.csv')

        # Concatenating all the sample files
        samples = pd.concat([sampleAug1_df, sampleAug2_df, sampleAug3_df, sampleSep1_df, sampleSep2_df, sampleSep3_df,sampleOct1_df, sampleOct2_df, sampleTillDate_df])
        len(samples) == len(sampleAug1_df) + len(sampleAug2_df) + len(sampleAug3_df) + len(sampleSep1_df) + len(sampleSep2_df) + len(sampleSep3_df) + len(sampleOct1_df) + len(sampleOct2_df) + len(sampleTillDate_df)

        #Keeping only the required columns for further analysis
        columns = ['Covid19Batch_id','eurofinsBarcode','PCRChannel1GeneName','PCRChannel1GeneCpValue',
                   'PCRChannel2GeneName','PCRChannel2GeneCpValue', 'ICRResult']
        samples_df = samples[columns]

        samples_batch_merge = pd.merge(samples_df, batch_df, how='left', on='Covid19Batch_id')

         #Filtering only for batchIDs starting with 'GE' & 'C_'
        samples_batch_merge=samples_batch_merge[(samples_batch_merge['batch_prefix']=='GE')|(samples_batch_merge['batch_prefix']=='C_')]

        top_senders_df = samples_batch_merge

        top_senders_df = top_senders_df[top_senders_df['machineName'].notnull()]

        top_senders_df

        top_senders_df.PCRChannel1GeneCpValue = top_senders_df.PCRChannel1GeneCpValue.replace(['-'], np.nan)
        top_senders_df.PCRChannel2GeneCpValue = top_senders_df.PCRChannel2GeneCpValue.replace(['-'], np.nan)
        top_senders_df.PCRChannel1GeneCpValue = pd.to_numeric(top_senders_df.PCRChannel1GeneCpValue)
        top_senders_df.PCRChannel2GeneCpValue = pd.to_numeric(top_senders_df.PCRChannel2GeneCpValue)

        top_senders_df.to_pickle('whole_merged_df.pkl')
        top_senders_df = pd.read_pickle('whole_merged_df.pkl')
        top_senders_df.ICRResult.isnull().sum()
        top_senders_df = top_senders_df[top_senders_df.ICRResult.notnull()]
        top_senders_df
        top_senders_df
        # Converting to date format
        top_senders_df['receptionDateTime'] = pd.to_datetime(top_senders_df['receptionDateTime'])
        top_senders_df['receptionDate'] = top_senders_df['receptionDateTime'].dt.date

        top_senders_df['clippingCompletionDateTime'] = pd.to_datetime(top_senders_df['clippingCompletionDateTime'])
        top_senders_df['clippingCompletionDate'] = top_senders_df['clippingCompletionDateTime'].dt.date
        top_senders_df
        top_senders_df.to_pickle('notNullICRdf_dates.pkl')
        top_senders_df = pd.read_pickle('notNullICRdf_dates.pkl')
        test = top_senders_df.copy()
        test
        test['receptionDate']=pd.to_datetime(test['receptionDateTime'])
        test.receptionDate
        test.index
        import datetime
        test['date_minus_time'] = test["receptionDate"].apply( lambda df : datetime.datetime(year=df.year, month=df.month, day=df.day))
        test.set_index(test["date_minus_time"],inplace=True)
        test
        len(test.index.unique())
        test.machineName = test.machineName.replace(['Aurora','TB-Aurora'], 'TB - Aurora')
        pop_std = pd.DataFrame(data = test['ICRResult'].resample('W').std())
        pop_std
        machine_std = pd.DataFrame(columns = ['machineName', 'len','date_minus_time', 'week_std'])
        machine_std
        machine_std['machineName'] = test.machineName.unique()
        machine_std
        for i in range(len(machine_std)):
            machine = machine_std.iloc[i,:]['machineName'] 
            machine_std.iloc[i,:]['len'] = len(test[test.machineName == machine]['ICRResult'].resample('W').std())
        machine_std
        machine_std = machine_std.reindex(machine_std.index.repeat(machine_std.len)).reset_index(drop=True)
        machine_std
        machine_std['date_minus_time'] = pd.to_datetime(machine_std['date_minus_time'])
        machine_std
        machine_names = test.machineName.unique()

        for i in range(len(machine_names)):
            machine_std.loc[machine_std.machineName == machine_names[i],'date_minus_time'] = test[test.machineName == machine_names[i]]['ICRResult'].resample('W').std().index
            machine_std.loc[machine_std.machineName == machine_names[i],'week_std'] = test[test.machineName == machine_names[i]]['ICRResult'].resample('W').std().values
        machine_std

        test[(test['machineName']=='TB - Pocahontas')&((test['date_minus_time'] >= '2020-10-18')&(test['date_minus_time'] < '2020-10-25'))]['ICRResult']
        test[(test['machineName']=='TB - Pocahontas')&((test['date_minus_time'] >= '2020-10-11')&(test['date_minus_time'] < '2020-10-18'))]['ICRResult']
        test[test.machineName == 'TB - Aurora']['ICRResult'].resample('W').mean()
        machine_std[machine_std.machineName == 'TB - Pocahontas']
        pop_std
        pop_std = pop_std.rename(columns = {'ICRResult': 'week_pop_std'})
        pop_std

        pop_std['group_pop_size'] = test['ICRResult'].resample('W').size().values
        pop_std

        merged_machine_std = pd.merge(machine_std, pop_std, how='left', on='date_minus_time')
        merged_machine_std

        merged_machine_std.to_pickle('merged_machine_std.pkl')
        merged_machine_std = pd.read_pickle('merged_machine_std.pkl')

        # # (population std - machine std)
        # merged_machine_std['week_std_diff'] = merged_machine_std.apply(lambda row: row.week_pop_std - row.week_std, axis = 1)

        # (machine std - population stf)
        merged_machine_std['week_std_diff'] = merged_machine_std.apply(lambda row: row.week_std - row.week_pop_std, axis = 1)

        merged_machine_std

        merged_machine_std = merged_machine_std.drop(['len'],axis=1)

        merged_machine_std

        # Calculating rolling avg and EMA
        for i in range(len(machine_names)):
            merged_machine_std.loc[merged_machine_std.machineName == machine_names[i],'rolling_avg'] = merged_machine_std[merged_machine_std.machineName == machine_names[i]]['week_std'].rolling(window=3).mean()
            merged_machine_std.loc[merged_machine_std.machineName == machine_names[i],'rolling_pop_avg'] = merged_machine_std[merged_machine_std.machineName == machine_names[i]]['week_pop_std'].rolling(window=3).mean()
            merged_machine_std.loc[merged_machine_std.machineName == machine_names[i],'ema_machine'] = merged_machine_std[merged_machine_std.machineName == machine_names[i]]['week_std'].ewm(span=3,adjust=False).mean()
            merged_machine_std.loc[merged_machine_std.machineName == machine_names[i],'ema_pop'] = merged_machine_std[merged_machine_std.machineName == machine_names[i]]['week_pop_std'].ewm(span=3,adjust=False).mean()


        merged_machine_std

        merged_machine_std.to_pickle('merged_machine_std_avg.pkl')
        merged_machine_std.to_csv('merged_machine_std.csv',index=False)

        from matplotlib import pyplot as plt

        #Individual EMA and Rolling average plots
        for i in range(len(machine_names)):
        # for i in range(2):
            df = merged_machine_std.loc[merged_machine_std.machineName == machine_names[i], ['date_minus_time',
                                                                                             'rolling_avg','rolling_pop_avg',
                                                                                            'ema_machine','ema_pop']]
            df.set_index('date_minus_time',inplace=True)

            #rolling avg
            df_roll = df.loc[:,['rolling_avg','rolling_pop_avg']]
            ax = df_roll.plot.line(title = 'Rolling average for STD for '+ machine_names[i],figsize=(20,10), style='.-')    
            plt.xlabel('Date')
            fig = ax.get_figure()
            fig.savefig('./plots/rolling/'+machine_names[i]+'_roll.jpg')

            #EMA
            df_ema = df.loc[:,['ema_machine','ema_pop']]
            ax = df_ema.plot.line(title = 'EMA for STD for '+ machine_names[i], figsize=(20,10), style='.-')
            plt.xlabel('Date')
            fig = ax.get_figure()
            fig.savefig('./plots/ema/'+machine_names[i]+'_ema.jpg')

        #EMA and Rolling average Subplots
        for i in range(len(machine_names)):
        # for i in range(2):
            df = merged_machine_std.loc[merged_machine_std.machineName == machine_names[i], ['date_minus_time',
                                                                                             'rolling_avg','rolling_pop_avg',
                                                                                            'ema_machine','ema_pop']]
            df.set_index('date_minus_time',inplace=True)

            nrow = 2
            ncol = 1

            #rolling avg
            df_roll = df.loc[:,['rolling_avg','rolling_pop_avg']]

            #EMA
            df_ema = df.loc[:,['ema_machine','ema_pop']]

            df_list = [df_roll, df_ema]
            fig, axes = plt.subplots(nrow, ncol)

            df_list[0].plot(ax=axes[0],title = 'Rolling average for STD for '+ machine_names[i],figsize=(20,10), style='.-', xlabel='Date')
            df_list[1].plot(ax=axes[1],title = 'EMA for STD for '+ machine_names[i], figsize=(20,10), style='.-', xlabel='Date')
            plt.tight_layout()
            fig.savefig('./plots/'+machine_names[i]+'.jpg')
        test[test.machineName == 'TB - Pocahontas']['ICRResult'].isnull().sum()
        # .resample('W').std() 


        test[test.machineName == 'TB - Pocahontas']   
        merged_machine_std = pd.read_pickle('merged_machine_std_avg.pkl')    
        test[test.machineName == 'TB - Pocahontas']['ICRResult'].resample('W').size().values 
        merged_machine_std

        merged_machine_std

        for i in range(len(machine_names)):
        # for i in range(2):
            merged_machine_std.loc[merged_machine_std.machineName == machine_names[i],'group_size'] = test[test.machineName == machine_names[i]]['ICRResult'].resample('W').size().values

        merged_machine_std

        for i in range(len(machine_names)):
        # for i in range(2):
            merged_machine_std.loc[merged_machine_std.machineName == machine_names[i],'group_size'] = test[test.machineName == machine_names[i]]['ICRResult'].resample('W').size().values

        merged_machine_std

        merged_machine_std.group_size = merged_machine_std.group_size.astype(int)
        merged_machine_std

        ftest = merged_machine_std.copy()

        ftest

        ftest['machine_var'] = ftest.apply(lambda x: x.week_std*x.week_std, axis = 1)

        ftest
        ftest['pop_var'] = ftest.apply(lambda x: x.week_pop_std*x.week_pop_std, axis = 1)
        ftest
        import scipy

        ftest['F'] = ftest.apply(lambda x: x.machine_var/x.pop_var, axis = 1)
        ftest

        ftest['p_value'] = ftest.apply(lambda row: 1-scipy.stats.f.cdf(row.F,row.group_pop_size-1, row.group_size-1) ,axis=1)
        # if (row.week_std_diff>0) else np.nan,axis=1)
        ftest
        ftest

        def f_test_inference(row):
            if row.week_std_diff>0:
                if row.p_value<0.05:
                    return 'Significantly different'
                else:
                    return 'Not significantly different'
            else:
                return 'Machine STD < Population STD'

        ftest['F_test_inference'] = ftest.apply(lambda row: f_test_inference(row), axis=1)
        ftest

        ftest['F_test_inference'] = ftest.apply(lambda row: f_test_inference(row), axis=1)
        ftest

        ftest.to_pickle('ftest_inf.pkl')

        cols = ['machineName', 'date_minus_time', 'week_std', 'machine_var','group_size','week_pop_std','pop_var','group_pop_size',
                'week_std_diff', 'rolling_avg', 'rolling_pop_avg','ema_machine', 'ema_pop', 'F','p_value', 'F_test_inference']
        ftest = ftest[cols]

        ftest.columns
        counts =pd.DataFrame(columns = ['Machine', 'Active Weeks', 'Significantly Different Weeks', 'Ratio'])
        counts['Machine'] = machine_names
        for i in range(len(counts)):
            machine = counts.iloc[i,:]['Machine'] 
            counts.iloc[i,:]['Active Weeks'] = len(test[test.machineName == machine]['ICRResult'].resample('W').std())

         counts
         len(ftest[(ftest.machineName == 'KF - Shirkan')&(ftest.F_test_inference=='Significantly different')])

        for i in range(len(counts)):
            counts.iloc[i,:]['Significantly Different Weeks'] = len(ftest[(ftest.machineName == machine_names[i])&(ftest.F_test_inference=='Significantly different')])
        counts

        counts['Ratio'] = counts.apply(lambda x: x['Significantly Different Weeks']/x['Active Weeks'], axis = 1)
        counts

        counts.to_csv('counts.csv',index=False)
        ftest.to_csv('ftest_result.csv', index=False)

        columns=['machineName','date_minus_time','F_test_inference']
        weekly_inference = ftest[columns]
        weekly_inference

        weeks = weekly_inference[weekly_inference.machineName=='KF - Shirkan']['date_minus_time']
        weeks

        def week_num(weeks, test):
            for i in range(len(weeks)):
                if test.date_minus_time == weeks[i]:
                    return ('Week - '+str(i+1))

        weekly_inference['week'] = weekly_inference.apply(lambda x: week_num(weeks,x),axis=1)
        weekly_inference

        weekly_inference

        def active_machine_week(c,test):
            b = []
            for i in range(len(test)):
                b.append('Week - '+str(i+1))
            return(b)

        for i in range(len(machine_names)):
        #     print(machine_names[i])
            weekly_inference.loc[weekly_inference.machineName==machine_names[i],'active_week_machine'] = active_machine_week(1,weekly_inference[weekly_inference.machineName==machine_names[i]])

        weekly_inference

        columns = ['machineName','date_minus_time','week','active_week_machine','F_test_inference']
        print(weekly_inference)
        weekly_inference = weekly_inference[columns]
        weekly_inference

        weekly_inference.to_csv('weekly_inference_weeklyforMachines.csv', index=False)
        ftest.to_csv('ftest_result_all.csv', index = False)   

        '''
    json_data = {'eurofine':script}
    return JsonResponse(json_data)
    # return HttpResponse(json_data, content_type='application/json')


def jsonData2(request):
    file1 = open('script_json/static/json_data.txt', 'r')
    Lines = file1.readlines()

    count = 1
    dict = {}
    # Strips the newline character
    for line in Lines:
        d = {count : line.strip()}
        dict.update(d)
        # print("Line{}: {}".format(count, line.strip()))
        count = count + 1
    # return JsonResponse(dict)
    json_data = json.dumps(dict)
    return HttpResponse(json_data,content_type='application/json')

