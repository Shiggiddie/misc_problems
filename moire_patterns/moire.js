(function() {
  var w = 500; //TODO base off of window.innerWidth or user input
  var h = 500; //TODO base off of window.innerHeight or user input
  var triangleW = 10; //TODO figure out how this is calculated
  var triangleH = Math.sqrt(3.0)*triangleW/2.0;  
  var d = w < h ? w : h; //TODO may not be necessary if page bounds are not of concern
  var numTriangles = Math.floor(d/triangleW);
  var numRows = Math.floor(d/triangleH);
  var triangle = '<div class="triangle"></div';
  var rotator = $('<div class="rotator"></div>');
  var bg = $('<div class="bg"></div>');

  //rotator.css('width', w);
  //rotator.css('height', w);

  for (var i = 0; i < numRows; i++) {
    var rRow = $('<div class="row"></div>');
    var bRow = $('<div class="row"></div>');

    for (var j = 0; j < numTriangles; j++) {
      var t1 = $(triangle);
      var t2 = $(triangle);

			// TODO add UI for turning colors on/off
      var a = ((j%3)+(i%3))%3;
      if (a==0) {
        t1.css('border-bottom-color', 'red');
        t2.css('border-bottom-color', 'red');
      } else if (a==1) {
        t1.css('border-bottom-color', 'blue');
        t2.css('border-bottom-color', 'blue');
      } else {
        t1.css('border-bottom-color', 'green');
        t2.css('border-bottom-color', 'green');
      }
      rRow.append(t1);
      bRow.append(t2);
    }
    rotator.append(rRow);
    bg.append(bRow);
  }

	//TODO add UI for rotation controls

  $('body').append(rotator);
  $('body').append(bg);
})()
