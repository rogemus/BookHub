const base = require('./webpack.make')('development');
const path = require('path');

module.exports = Object.assign(
	{},
	base,
	{
		devServer: {
			contentBase: path.join(__dirname, 'public'),
			host: '0.0.0.0',
			port: 8000,
			proxy: [{
				context: ['/accounts', '/api'],
				target: 'http://backend:8080'
			}]
		}
	}
);
