from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import word_cloud
import topic_modeling

file_path="input_esm.xlsx"  #Please put the excel file into the same folder as this code
raw_data=pd.read_excel(file_path)


def extract_notask(data):
    '''
    Extracts no_task_why and do_later_when categories for suvey
    participants that did not complete any tasks

    Excludes all of the nan (did not have answer) values
    '''
    no_task_why=[]
    do_later_when=[]
    for index, row in data.iterrows():
        if pd.isna(row["Completed.Tasks"]):
            no_task_why.append(row["NoTask.Why?"])
            do_later_when.append(row["DoLater.When?"])
            no_task_why=pd.Series(no_task_why).dropna().tolist()
            do_later_when=pd.Series(do_later_when).dropna().tolist()
    return (no_task_why,do_later_when)

(no_task_why,do_later_when)=extract_notask(raw_data)




"Word cloud generation"
word_cloud.generate_word_cloud(no_task_why)
word_cloud.generate_word_cloud(do_later_when)


"Topic Modeling"

no_task_why_topic=topic_modeling.topic_modeling(no_task_why)
do_later_when_topic=topic_modeling.topic_modeling(do_later_when)

print("Topic Modeling for No_Task_Why")
for i, topic in enumerate(no_task_why_topic):
    print(f"Topic {i+1}: {', '.join(topic)}")


print("Topic Modeling for do_later_when")
for i, topic in enumerate(do_later_when_topic):
    print(f"Topic {i+1}: {', '.join(topic)}")



def classify_by_cond(data,condition):
    task_why=[]
    task_challenge=[]
    task_resource=[]
    task_help_others=[]
    task_discussed=[]
    for index, row in data.iterrows():
        if (not pd.isna(row["Completed.Tasks"])):
            if row["Cond"]==condition:
                task_why.append(row["TaskA.Why?"])
                task_challenge.append(row["TaskA.Challenges.Text"])
                task_resource.append(row["TaskA.Resources.Text"])
                task_help_others.append(row["TaskA.HelpOthers"])
                task_discussed.append(row["TaskA.Discussed.Text"])
    task_why=pd.Series(task_why).dropna().tolist()
    task_challenge=pd.Series(task_challenge).dropna().tolist()
    task_resource=pd.Series(task_resource).dropna().tolist()
    task_help_others=pd.Series(task_help_others).dropna().tolist()
    task_discussed=pd.Series(task_discussed).dropna().tolist()
    return [task_why,task_challenge,task_resource,task_help_others,task_discussed]


adulting_set=classify_by_cond(raw_data,"1")

cybersecurity_set=classify_by_cond(raw_data,"2")

"word cloud generation"


for text_list in adulting_set:
    word_cloud.generate_word_cloud(text_list)

for text_list in cybersecurity_set:
    word_cloud.generate_word_cloud(text_list)

"Topic Modeling"

"Currently with only task A, task help cannot be topic-modeled for both conditions due to too less datapoints"
#adulting_topics = [topic_modeling.topic_modeling(task_info) for task_info in adulting_set]
#Ecybersecurity_topics=[topic_modeling.topic_modeling(task_info) for task_info in cybersecurity_set]


def extract_buddy_info(data):
    buddy_info=[]
    for index, row in data.iterrows():
        buddy_info.append(row["Q185_6_TEXT"])
        buddy_info.append(row["Q188"])
        buddy_info.append(row["Q186"])
        #print(buddy_info)
    buddy_info=pd.Series(buddy_info).dropna().tolist()
    return buddy_info

buddy_info=extract_buddy_info(raw_data)

"Word cloud Generation"
word_cloud.generate_word_cloud(buddy_info)

"Topic Modeling"
buddy_topic=topic_modeling.topic_modeling(buddy_info)

print("Topic Modeling for buddy_questions")
for i, topic in enumerate(buddy_topic):
    print(f"Topic {i+1}: {', '.join(topic)}")


def extract_Q187(data):
    question=[]
    for index, row in data.iterrows():
       question.append(row["Q187"])
    question=pd.Series(question).dropna().tolist()
    return question

question_187=extract_Q187(raw_data)

"Word Cloud Generation"
word_cloud.generate_word_cloud(question_187)

"Topic Modeling"
question_187_topic=topic_modeling.topic_modeling(question_187)
print("Topic Modeling for Q187")
for i, topic in enumerate(question_187_topic):
    print(f"Topic {i+1}: {', '.join(topic)}")

    














