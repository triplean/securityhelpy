import 'package:translator/translator.dart';

Future<String> translate(String text, String targetLanguage) async {
    final tranlator = GoogleTranslator();
    final translation = await tranlator.translate(text, to: targetLanguage);
    return translation.text;
  }