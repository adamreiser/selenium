/*
Sometimes Selenium is not the best tool.
PhantomJS is much faster.

*/

var page = require('webpage').create();
var url = 'http://localhost:8000';
var out = 'wiki_phantomjs.png'

page.viewportSize = { width: 1024, height: 768 };

page.open(url, function (status) {
	if (status !== 'success') {
		phantom.exit(1);
	} else {
		window.setTimeout(function () {
			page.render(out);
			phantom.exit();
		}, 200);
	}
});
