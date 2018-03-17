const base = require('./webpack.make')();
const path = require('path');

module.exports = Object.assign(
	{},
	base,
	{
		devServer: {
			contentBase: path.join(__dirname, 'public'),
			port: 8000
		}
	}
);
