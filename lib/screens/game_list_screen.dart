import 'package:flutter/material.dart';
import '../services/guide_service.dart';
import '../models/guide_model.dart';
import 'guide_detail_screen.dart';

class GameListScreen extends StatefulWidget {
  @override
  _GameListScreenState createState() => _GameListScreenState();
}

class _GameListScreenState extends State<GameListScreen> {
  late Future<List<GuideModel>> _futureGuides;
  List<GuideModel> _guides = [];
  List<GuideModel> _filteredGuides = [];
  String _searchText = '';

  @override
  void initState() {
    super.initState();
    _futureGuides = GuideService().fetchGuides();
    _futureGuides.then((guides) {
      setState(() {
        _guides = guides;
        _filteredGuides = guides;
      });
    });
  }

  void _filterGuides(String searchText) {
    setState(() {
      _searchText = searchText.toLowerCase();
      _filteredGuides = _guides.where((guide) {
        final title = guide.title.toLowerCase();
        final game = guide.game.toLowerCase();
        return title.contains(_searchText) || game.contains(_searchText);
      }).toList();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Row(
          children: [
            // Cargar la imagen local y redimensionarla
            Image.asset(
              'assets/logo.png',  // Reemplaza con la ruta correcta de la imagen
              height: 40,                 // Ajusta el tamaño de la imagen
              width: 40,                  // Ajusta el tamaño de la imagen
            ),
            SizedBox(width: 16),
            Expanded(
              child: TextField(
                decoration: InputDecoration(
                  hintText: '¿Buscas algo?',
                  hintStyle: TextStyle(color: Colors.black),
                ),
                style: TextStyle(color: Colors.black),
                onChanged: _filterGuides,
              ),
            ),
          ],
        ),
      ),
      body: FutureBuilder<List<GuideModel>>(
        future: _futureGuides,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            return Center(child: Text('Error al cargar guías'));
          } else if (_filteredGuides.isEmpty) {
            return Center(child: Text('No se encontraron guías'));
          }

          return ListView.builder(
            itemCount: _filteredGuides.length,
            itemBuilder: (context, index) {
              final guide = _filteredGuides[index];
              return ListTile(
                title: Text(guide.title),
                subtitle: Text('Juego: ${guide.game}'),
                onTap: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) => GuideDetailScreen(guide: guide),
                    ),
                  );
                },
              );
            },
          );
        },
      ),
    );
  }
}
