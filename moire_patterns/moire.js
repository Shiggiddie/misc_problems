var numTriangles = 50;
var triangle = '<div class="arrow-up"></div';
var rotator = $('<div class="rotator"></div>');
var bg = $('<div class="bg"></div>');

for (var i = 0; i < numTriangles; i++) {
	var rRow = $('<div class="row"></div>');
	var bRow = $('<div class="row"></div>');

	for (var j = 0; j < numTriangles; j++) {
		rRow.append(triangle);
		bRow.append(triangle);
	}
  rotator.append(rRow);
  bg.append(bRow);
	console.log('time through');
	console.log(rotator);
}

$('body').append(rotator);
$('body').append(bg);
