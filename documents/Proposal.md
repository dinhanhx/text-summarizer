# Project name: Text Summarizer

**Document owner**

- Nguyen Lan Huong ~ BI9-114
- Dao Duong Hoang Long ~ BI9-154 
- Nguyen Nhu Hieu BI9 ~ BI9-103
- Vu Dinh Anh ~ BI9-037

**Table of Contents**

1        [Background](https://github.com/dinhanhx/text-summarizer/blob/master/documents/Proposal.md#1-background)

2        [Proposal](https://github.com/dinhanhx/text-summarizer/blob/master/documents/Proposal.md#2-proposal)

&nbsp;&nbsp;2.1        [Vision and Goals](https://github.com/dinhanhx/text-summarizer/blob/master/documents/Proposal.md#21-vision-and-goals)

&nbsp;&nbsp;2.2        [Plans](https://github.com/dinhanhx/text-summarizer/blob/master/documents/Proposal.md#22-plans)

&nbsp;&nbsp;2.3        [Risks &amp; Issues](https://github.com/dinhanhx/text-summarizer/blob/master/documents/Proposal.md#23-risks--issues)

&nbsp;&nbsp;2.4        [Success Criteria](https://github.com/dinhanhx/text-summarizer/blob/master/documents/Proposal.md#24-success-criteria)

&nbsp;&nbsp;2.5        [Authorization](https://github.com/dinhanhx/text-summarizer/blob/master/documents/Proposal.md#25-authorization)


## 1. Background

When reading a piece of text such as an article or a textbook, one ought to draw a clear overview of the subject to have a solid understanding of key concepts. However, it is sometimes a stressful job eliciting the most fundamental information from massive walls of tex. Additionally, some important information may be missed or left out during the process.


## 2. Proposal


### 2.1 Vision and Goals

Our team has the intention to build a text summarizer, which means it can receive a text file as input and simplify it down to only the most fundamental information such as key words. The process is simple: the user inputs a pdf and wait. The software processes the file and exports a new one, containing only the summarization.

This software can be helpful tool for students to learn textbooks and articles productively. Moreover, lecturers can benefit from it when designing lecture slides based on textbooks.

An [example](http://autosummarizer.com/) of a similar software: 

The most fundamental function of the software is to return a list of keywords. If our team has more time, we can organize this list in this order: key concepts - brief explanation - conclusion.

### 2.2 Plans

Front-end: The interface in design can be found [here](https://www.figma.com/file/ZSctHH5q0kA7mcsh6l9EZK/UI-text-summarizer)

Back-end: Our team is going to build a neural network on the Python platform to classify keywords. The kernel we plan to use can be found [here](https://www.kaggle.com/au1206/text-classification-using-cnn)

Framework: [Flutter](https://flutter.dev/docs/deployment/web) for Web app

### 2.3 Risks &amp; Issues

| **Project Risks** |

The model may derive an imprecise classification of the text, namely omitting key words and keep around unimportant information.
This largely depends on the efficiency of our algorithm. The more we optimize it, the less likely this problem occurs.


| **Project Issues** |


1. Our team consists of unexperienced coders.

2. We do not have a big enough data base to train the model.

3. We only have access to a few open-source libraries for text mining.


### 2.4 Success Criteria

1. The model at least works smoothly with simple text files and return key information.
2. The software can create an average quality summarization of real textbooks, which is mark 5 to 6 out of 10. Users can test the software and give the mark as their assessment.
3. Grow our data base to further improve the model in the future.

### 2.5 Authorization
**Professor** Truong Anh Hoang
