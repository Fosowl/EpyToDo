
		function my_draw_square(square, x, y, color) {
			square.beginPath();
			square.rect(x, y, 30, 10);
			square.fillStyle = color;
			square.strokeStyle = color;
			square.fill;
			square.lineWidth = 20;
			square.stroke();
		}


		function my_draw_circle(circle, x, y, turn, color, size) {
			circle.beginPath();
			x += 30;
			circle.arc(x, y, size, 0, (Math.PI * 2) * turn, false);
			circle.fillStyle = color;
			circle.strokeStyle = color;
			circle.lineWidth = 7;
			circle.stroke();
		}

		function load_json() {
			var json;
			var file;
			var requestURL = './data.json'
			var request = new XMLHttpRequest;

			request.open('GET', requestURL);
			request.responseType = 'json';
			request.send();
			request.onload = function() {
				var file = request.response;
			}
			json = JSON.parse(file);
			return json;
		}