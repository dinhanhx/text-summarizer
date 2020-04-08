import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:text_summarizer/view/home/home_view.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
        title: 'Text Summarizer',
        theme: ThemeData(
          primarySwatch: Colors.blue,
        ),
        home: HomeView()
    );
  }
}



