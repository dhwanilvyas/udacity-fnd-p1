$(document).on("click",".movie_tile", function () {
	var trailerYouTubeId = $(this).attr('data-movie-id');
	$.get("https://api.themoviedb.org/3/movie/" + trailerYouTubeId + "/videos?api_key=7b7239657b20c59003be4fdd339956cf", function(data) {
		var id = data.results[0].key;
		window.open('https://youtube.com/watch?v=' + id, '_blank');
	});
});
