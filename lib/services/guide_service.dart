import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/guide_model.dart';
import 'translate_service.dart';


class GuideService {
  final String apiUrl = 'https://triplean.vercel.app/r/sh/glist.json';

  Future<List<GuideModel>> fetchGuides() async {
    final response = await http.get(Uri.parse(apiUrl));

    if (response.statusCode == 200) {
      final List<dynamic> jsonResult = json.decode(response.body);
      List<GuideModel> guides = [];

      for (var json in jsonResult) {
        // Create a new map to hold the translated values
        Map<String, dynamic> translatedJson = {};

        // Iterate through each key-value pair in the JSON
        for (var entry in json.entries) {
          if (entry.key != 'imageUrls' && entry.value is String) {
            // Translate the string value
            final translatedValue = await translate(entry.value, 'en');
            translatedJson[entry.key] = translatedValue; // Add translated value
          } else {
            // Keep the original value for imageUrls and non-string values
            translatedJson[entry.key] = entry.value;
          }
        }

        // Create the GuideModel from the translated map
        guides.add(GuideModel.fromMap(translatedJson));
      }
      return guides;
    } else {
      throw Exception('Error al cargar guías');
    }
  }
}