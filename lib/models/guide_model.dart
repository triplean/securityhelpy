class GuideModel {
  final int id;
  final String title;
  final String content;
  final String game;
  final List<String> imageUrls;

  GuideModel({
    required this.id,
    required this.title,
    required this.content,
    required this.game,
    required this.imageUrls,
  });

  factory GuideModel.fromMap(Map<String, dynamic> json) {
    return GuideModel(
      id: json['id'],
      title: json['title'],
      content: json['content'],
      game: json['game'],
      imageUrls: List<String>.from(json['imageUrls'] ?? []),
    );
  }

  Map<String, dynamic> toMap() {
    return {
      'id': id,
      'title': title,
      'content': content,
      'game': game,
      'imageUrls': imageUrls,
    };
  }
}
