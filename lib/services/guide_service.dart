import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/guide_model.dart';

class GuideService {
  final String apiUrl = 'https://triplean.vercel.app/r/sh/glist.json';

  Future<List<GuideModel>> fetchGuides() async {
    final response = await http.get(Uri.parse(apiUrl));

    if (response.statusCode == 200) {
      final List<dynamic> jsonResult = json.decode(response.body);
      return jsonResult.map((json) => GuideModel.fromMap(json)).toList();
    } else {
      throw Exception('Error al cargar guías');
    }
  }
}
