# Project name: Text Summarizer
# Project Proposal:

**Document owner**

Vu Dinh Anh,
Nguyen Lan Huong,
Nguyen Nhu Hieu,
Dao Duong Hoang Long

**Table of Contents**

1        Background

2        Proposal

2.1        Vision and Goals

2.2        Plans

2.2        Risks &amp; Issues

2.3        Implications

2.4        Success Criteria

2.5        Authorization


## 1. Background

Studying at university requires a significant amount of work, especially when it comes to exams. To study efficiently, a student ought to draw a clear overview of the course and have a solid understanding of key concepts in the subject.

However, it is sometimes a stressful job eliciting the most fundamental information from massive walls of text from the books and lecture notes. In addition, some important information may be missed or left out during the process, which may lead to unsatisfying exam results.


## 2. Proposal


### 2.1 Vision and Goals

Our team has the intention to build a software which can automatically summarize a pdf file, namely a textbook or lecture notes, and simplify it down to only the most fundamental information, such as key words, definitions, theorems and so on.

The process is simple: the user inputs a pdf and wait. The software processes the file and exports a new one, containing only the summarization.

This software can be helpful tool for students to learn productively and absorb knowledge easily. Moreover, lecturers can benefit from it when designing lecture slides based on textbooks.

### 2.2 Plans

Our team is going to build a neural network to classify words in the text and elicit the most important keywords.
Our platform is going to be Python and the kernel we plan to use can be found [here.](https://www.kaggle.com/au1206/text-classification-using-cnn)

Besides, we are going to implement our application's UI with Figma. [Click here.](https://www.figma.com/file/ZSctHH5q0kA7mcsh6l9EZK/UI-text-summarizer?node-id=0%3A1)

### 2.2 Risks &amp; Issues

| **Project Risks** |

1. Unable to elicit headers and key words

Sometimes, there can be little or no difference between the appearance or format of key information to the rest, for example they all have the same font size, same color, no special sign, no indentation.

Whether this problem happens or not depends on the format and presentation of the book. If the book does provide a clear contrast between different classes of information, the software cannot function right.

2. Miss out on important information

The algorithm of the software can derive an imprecise classification of texts from the file, omitting key words and keep around irrelevant or excess pieces of information.

This largely depends on the efficiency of our algorithm. The more we improve and perfect it, the less likely this problem occurs.


| **Project Issues** |


1. Our team consists of new programmers with limited coding skills.


2. We do not have a big enough data base to learn from and build the software.

3. We are not experienced in this field.


### 2.3 Implications

### 2.4 Success Criteria

1. The software at least works smoothly with simple text files. Simple means the format is commonly seen, for example: header - explanation - conclusion, and the presentation of the file is clear.
2. The software can create an average quality summarization of real textbooks, which is mark 5 to 6 out of 10. Users can test the software and give the mark as their assessment.
3. Grow out data base to further improve the software in the future.

### 2.5 Authorization
**Professor** Truong Anh Hoang
