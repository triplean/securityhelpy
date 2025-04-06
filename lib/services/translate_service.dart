import 'dart:convert';
import 'package:http/http.dart' as http;

class TranslateService {
  final String apiUrl = 'https://libretranslate.de/translate';

  Future<String> translate(String text, String targetLanguage) async {
    final response = await http.post(
      Uri.parse(apiUrl),
      headers: {
        'Content-Type': 'application/json',
      },
      body: json.encode({
        'q': text,
        'source': 'en',
        'target': targetLanguage,
        'format': 'text',
      }),
    );

    if (response.statusCode == 200) {
      final responseBody = json.decode(response.body);
      return responseBody['translatedText'];
    } else {
      throw Exception('Error al traducir el texto');
    }
  }
}
