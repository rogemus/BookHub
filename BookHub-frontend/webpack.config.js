// http://webpack.github.io/docs/configuration.html
// http://webpack.github.io/docs/webpack-dev-server.html
var path = require('path');
var CleanWebpackPlugin = require('clean-webpack-plugin');

module.exports = {
	entry: [
		'webpack-dev-server/client?http://localhost:8000',
		'webpack/hot/only-dev-server',
		'babel-polyfill',
		__dirname + '/src/index.js'
	],
	output: {
		path: __dirname + '/public/js',
		publicPath: 'js/',
		filename: 'bundle.js'
	},
	module: {
		rules: [
			{
				test: /\.js$/,
				loaders: ['react-hot-loader', 'babel'],
				exclude: /node_modules/
			},
			{
				// https://github.com/jtangelder/sass-loader
				test: /\.scss$/,
				loaders: ['style', 'css', 'sass']
			},
			{
				test: /\.css$/,
				loaders: ['style', 'css']
			}
		]
	},
	devServer: {
		contentBase: __dirname + '/public'
	},
	plugins: [
		new CleanWebpackPlugin(['css/main.css', 'js/bundle.js'], {
			root: __dirname + '/public',
			verbose: true,
			dry: false // true for simulation
		})
	]
};
