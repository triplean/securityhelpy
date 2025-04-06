import 'package:flutter/material.dart';
import 'screens/game_list_screen.dart';

void main() {
  runApp(SecurityHelpy());
}

class SecurityHelpy extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Security Helpy',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: GameListScreen(),
    );
  }
}
