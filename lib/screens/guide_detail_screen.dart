import 'package:flutter/material.dart';
import '../models/guide_model.dart';
import 'package:flutter_image_slideshow/flutter_image_slideshow.dart';

class GuideDetailScreen extends StatelessWidget {
  final GuideModel guide;

  GuideDetailScreen({required this.guide});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(guide.title)),
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: ListView(
          children: [
            Text(
              'Juego: ${guide.game}',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 16),
            Text(
              guide.content,
              style: TextStyle(fontSize: 16),
            ),
            SizedBox(height: 16),
            if (guide.imageUrls.isNotEmpty)
              SizedBox(
                height: 300, // Ajusta el tamaño según sea necesario
                child: ImageSlideshow(
                  children: guide.imageUrls.map((url) {
                    return Image.network(
                      url,
                      fit: BoxFit.contain,
                      width: double.infinity,
                    );
                  }).toList(),
                ),
              ),
          ],
        ),
      ),
    );
  }
}
