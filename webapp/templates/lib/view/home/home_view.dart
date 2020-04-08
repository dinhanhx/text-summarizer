import 'package:flutter/material.dart';
import 'package:text_summarizer/widgets/app_detail/app_detail.dart';
import 'package:text_summarizer/widgets/centered_view/centered_view.dart';
import 'package:text_summarizer/widgets/navigation_bar/navigation_bar.dart';
import 'package:text_summarizer/widgets/uploads/uploads.dart';

class HomeView extends StatelessWidget {
  const HomeView({Key key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      body: CenteredView(
              child: Column(children: <Widget>[
          NavigationBar(),
          Expanded(child: Row(children: <Widget>[
            AppDetail(),
            Expanded(child: Center(child: Uploads('Upload file here'),))
          ],))
        ],),
      ),
    );
  }
}



