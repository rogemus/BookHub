const path = require('path');
const webpack = require('webpack');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
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
					test: /\.scss$/,
					use: ExtractTextPlugin.extract({
						fallback: 'style-loader',
						use: [
							{
								loader: 'css-loader?-url'
							},
							{
								loader: 'postcss-loader'
							},
							{
								loader: 'sass-loader'
							}
						]
					})
				},
				{
					test: /\.html$/,
					use: ['html-loader']
				}
			]
		},
		plugins: [
			new ExtractTextPlugin('bundle.css', {
				allChunks: true
			}),
			new StyleLintPlugin({
				configFile: '.stylelintrc.json'
			}),
			new FriendlyErrorsWebpackPlugin()
		],
		devtool: 'eval-source-map',
		node: {
			fs: 'empty'
		}
	};
};
