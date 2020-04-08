import 'package:flutter/material.dart';

class AppDetail extends StatelessWidget {
  const AppDetail({Key key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 600,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          Text('Text Sumarizer.\nWhat do i do',
          style: TextStyle(fontWeight: FontWeight.w800,height: 0.9,fontSize: 70),
          ),
          SizedBox(height: 30,),
          Text('The Text Summarizing Software is a tool to analyze text documents and simplify them to only the key words. It captures most significant concepts, providing a concise overview, which can be useful in studying and memorizing for the user. The software is applicable to a myriad of documents such as articles or textbooks; and supports typical text files or online articles.',
          style: TextStyle(fontSize: 21, height:1.7))
        ],
      ),
    );
  }
}