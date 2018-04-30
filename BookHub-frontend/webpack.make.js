const path = require('path');
const webpack = require('webpack');
const FriendlyErrorsWebpackPlugin = require('friendly-errors-webpack-plugin');

require('babel-polyfill');

module.exports = (mode) => {
	return {
		entry: {
			'bundle': ['babel-polyfill', './src/index.js']
		},
		output: {
			path: `${__dirname}/public`,
			filename: '[name].js',
			chunkFilename: '[name].js'
		},
		stats: {
			warnings: false
		},
		resolve: {
			alias: {
				'react': path.resolve(path.join(__dirname, 'node_modules', 'react'))
			}
		},
		module: {
			rules: [
				{
					test: /\.js$/,
					exclude: /node_modules/,
					use: [
						'babel-loader',
						'eslint-loader'
					]
				},
				{
					test: /\.scss$/,
					use: [
						{
							loader: 'style-loader'
						},
						{
							loader: 'css-loader'
						},
						{
							loader: 'sass-loader'
						}
					]
				}
			]
		},
		mode: mode,
		plugins: [
			new FriendlyErrorsWebpackPlugin()
			//new BundleAnalyzerPlugin()
		],
		devtool: 'source-map',
		node: {
			fs: 'empty'
		}
	};
};
