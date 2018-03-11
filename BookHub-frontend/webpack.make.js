const path = require('path');
const webpack = require('webpack');
const StyleLintPlugin = require('stylelint-webpack-plugin');
const FriendlyErrorsWebpackPlugin = require('friendly-errors-webpack-plugin');

require('babel-polyfill');

module.exports = (options) => {
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
					test: /\.css$/,
					use: [
						'style-loader',
						{loader: 'css-loader', options: {importLoaders: 1}},
						'postcss-loader'
					]
				}
			]
		},
		plugins: [
			new StyleLintPlugin({
				configFile: '.stylelintrc.json'
			}),
			new FriendlyErrorsWebpackPlugin()
		],
		devtool: 'source-map',
		node: {
			fs: 'empty'
		}
	};
};
